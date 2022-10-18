from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from .core import VElement, VNode, VString
from .utils import ElementId, ScopeId

if TYPE_CHECKING:
    from .scope import Scopes

@dataclass
class PushRoot:
    type = "PushRoot"
    root: ElementId

@dataclass
class AppendChildren:
    type = "AppendChildren"
    many: int

@dataclass
class ReplaceWith:
    type = "ReplaceWith"
    root: ElementId
    many: int

@dataclass
class InsertAfter:
    type = "InsertAfter"
    root: ElementId
    many: int

@dataclass
class InsertBefore:
    type = "InsertBefore"
    root: ElementId
    many: int

@dataclass
class Remove:
    type = "Remove"
    root: ElementId

@dataclass
class CreateTextNode:
    type = "CreateTextNode"
    root: ElementId
    text: str

@dataclass
class CreateElement:
    type = "CreateElement"
    root: ElementId
    tag: str

@dataclass
class CreatePlaceholder:
    type = "CreatePlaceholder"
    root: ElementId

@dataclass
class NewEventListener:
    type = "NewEventListener"
    event_name: str
    scope: ScopeId
    root: ElementId

@dataclass
class SetText:
    type = "SetText"
    root: ElementId
    text: str

@dataclass
class SetAttribute:
    type = "SetAttribute"
    root: ElementId
    field: str
    value: Any

@dataclass
class RemoveAttribute:
    type = "RemoveAttribute"
    root: ElementId
    name: str

@dataclass
class PopRoot:
    type = "PopRoot"


Modification = PushRoot | AppendChildren | ReplaceWith | InsertAfter | InsertBefore | Remove | CreateTextNode | CreateElement | CreatePlaceholder | NewEventListener | SetText | SetAttribute | RemoveAttribute | PopRoot


class Mutations:
    def __init__(self):
        self.modifications: list[Modification] = []
        self.dirty_scopes: list[ScopeId] = []

    def append(self, mod: Modification):
        self.modifications.append(mod)

    def mark_dirty(self, scope_id: ScopeId):
        self.dirty_scopes.append(scope_id)

    def serialize(self) -> list[dict[str, Any]]:
        return [mod.__dict__ | {"type": mod.type} for mod in self.modifications]


class Diff:
    def __init__(self, scopes: Scopes):
        self.scopes = scopes
        self.mutations = Mutations()
        self.force_diff = False
        self.element_stack: list[ElementId] = []
        self.scope_stack: list[ScopeId] = []

    def diff_scope(self, scope_id: ScopeId):
        scope = self.scopes.get_scope(scope_id)
        old = scope.wip_frame()
        new = scope.fin_frame()

        self.scope_stack.append(scope_id)
        self.element_stack.append(scope.container)

        self.diff(old, new)

        self.element_stack.pop()
        self.scope_stack.pop()

        self.mutations.mark_dirty(scope_id)

    def diff(self, old: VNode, new: VNode):
        match old, new:
            case VString() as old, VString() as new:
                self.diff_string_nodes(old, new)
            case VElement() as old, VElement() as new:
                self.diff_element_nodes(old, new)
            case _:
                self.replace_node(old, new)

    def diff_string_nodes(self, old: VString, new: VString):
        if old.data != new.data:
            self.mutations.append(SetText(new.id, new.data))

        self.scopes.update_node(new, old.id)

    def diff_element_nodes(self, old: VElement, new: VElement):
        if new.tag != old.tag:
            return self.replace_node(old, new)

        self.scopes.update_node(new, old.id)

    def replace_node(self, old: VNode, new: VNode):
        created = self.create_node(new)
        self.replace_inner(old, created)

    def create_node(self, node: VNode) -> int:
        match node:
            case VString() as node:
                return self.create_string_node(node)
            case VElement() as node:
                return self.create_element_node(node)
            case _:
                return 0

    def replace_inner(self, node: VNode, created: int):
        match node:
            case VString() as node:
                self.mutations.append(ReplaceWith(node.id, created))

            case VElement() as node:
                self.mutations.append(ReplaceWith(node.id, created))
                self.remove_nodes(node.children, False)
                self.scopes.remove_node(node.id)

            case _:
                pass

    def remove_nodes(self, nodes: list[VNode], gen_muts: bool):
        for node in nodes:
            match node:
                case VString() as node:
                    self.scopes.remove_node(node.id)

                    if gen_muts:
                        self.mutations.append(Remove(node.id))

                case VElement() as node:
                    if gen_muts:
                        self.mutations.append(Remove(node.id))

                    self.scopes.remove_node(node.id)
                    self.remove_nodes(node.children, False)

                case _:
                    pass

    def create_string_node(self, node: VString) -> int:
        self.scopes.update_node(node, node.id)

        self.mutations.append(CreateTextNode(node.id, node.data))
        return 1

    def create_element_node(self, node: VElement) -> int:
        self.scopes.update_node(node, node.id)
        node.parent_id = self.element_stack[-1]
        self.element_stack.append(node.id)
        self.mutations.append(CreateElement(node.id, node.tag))

        scope_id = self.current_scope()

        for listener in node.listeners:
            self.mutations.append(NewEventListener(listener.name, scope_id, node.id))

        for key, value in node.attributes.values():
            self.mutations.append(SetAttribute(node.id, key, value))

        if children := node.children:
            self.create_and_append_children(children)

        self.element_stack.pop()

        return 1

    def create_and_append_children(self, nodes: list[VNode]):
        created = self.create_children(nodes)
        self.mutations.append(AppendChildren(created))

    def create_children(self, nodes: list[VNode]) -> int:
        for node in nodes:
            self.create_node(node)

        return len(nodes)

    def current_scope(self) -> ScopeId:
        return self.scope_stack[-1]
