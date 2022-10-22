from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, cast

from .core import VComponent, VElement, VNode, VPlaceholder, VString
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
    root: ElementId
    children: list[ElementId]

@dataclass
class ReplaceWith:
    type = "ReplaceWith"
    root: ElementId
    nodes: list[ElementId]

@dataclass
class InsertAfter:
    type = "InsertAfter"
    root: ElementId
    nodes: list[ElementId]

@dataclass
class InsertBefore:
    type = "InsertBefore"
    root: ElementId
    nodes: list[ElementId]

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
        self.scope_stack: list[ScopeId] = []

    def diff_scope(self, parent_id: ElementId, scope_id: ScopeId):
        scope = self.scopes.get_scope(scope_id)
        old = scope.wip_frame()
        new = scope.fin_frame()

        self.scope_stack.append(scope_id)

        self.diff_node(parent_id, old, new)

        self.scope_stack.pop()

        self.mutations.mark_dirty(scope_id)

    def diff_node(self, parent_id: ElementId, old: VNode, new: VNode):
        match old, new:
            case VString() as old, VString() as new:
                self.diff_string_nodes(old, new)
            case VElement() as old, VElement() as new:
                self.diff_element_nodes(old, new)
            case _:
                self.replace_node(parent_id, old, new)

    def diff_string_nodes(self, old: VString, new: VString):
        if old is new:
            return

        element_id = old.id if old.id is not None else self.scopes.reserve_node(new)

        if old.data != new.data:
            self.mutations.append(SetText(element_id, new.data))

        self.scopes.update_node(new, element_id)
        new.id = element_id

    def diff_element_nodes(self, old: VElement, new: VElement):
        if old is new:
            return

        element_id = old.id if old.id is not None else self.scopes.reserve_node(new)

        if new.tag != old.tag:
            return self.replace_node(element_id, old, new)

        self.scopes.update_node(new, element_id)
        new.id = element_id
        new.parent_id = old.parent_id

        # todo diff attributes and listeners

        match old.children, new.children:
            case [], []:
                pass

            case [], new_children:
                created = []
                self.create_children(element_id, new_children, created)
                self.mutations.append(AppendChildren(element_id, created))

            case old_children, new_children:
                self.diff_children(element_id, old_children, new_children)

    def diff_children(self, parent_id: ElementId, old: list[VNode], new: list[VNode]):
        old_len = len(old)
        new_len = len(new)

        if old_len > new_len:
            self.remove_nodes(old[new_len:], True)
        elif old_len < old_len:
            self.create_and_insert_after(parent_id, new[old_len:], old[-1])

        for new_node, old_node in zip(new, old):
            self.diff_node(parent_id, old_node, new_node)

    def replace_node(self, parent_id: ElementId, old: VNode, new: VNode):
        nodes: list[ElementId] = []
        self.create_node(parent_id, new, nodes)
        self.replace_inner(old, nodes)

    def create_node(self, parent_id: ElementId, node: VNode, nodes: list[ElementId]):
        match node:
            case VString() as node:
                self.create_string_node(node, nodes)
            case VElement() as node:
                self.create_element_node(parent_id, node, nodes)
            case VPlaceholder() as node:
                self.create_placeholder_node(node)
            case VComponent() as node:
                self.create_componet_node(parent_id, node, nodes)

    def replace_inner(self, node: VNode, nodes: list[ElementId]):
        match node:
            case VString() | VPlaceholder():
                element_id = cast(ElementId, node.id)

                self.mutations.append(ReplaceWith(element_id, nodes))
                self.scopes.remove_node(element_id)

            case VElement() as node:
                element_id = cast(ElementId, node.id)
                self.mutations.append(ReplaceWith(element_id, nodes))
                self.remove_nodes(node.children, False)
                self.scopes.remove_node(element_id)

            case VComponent() as node:
                scope_id = node.scope_id
                assert scope_id is not None

                scope = self.scopes.get_scope(scope_id)
                inner_node = scope.fin_frame()

                self.enter_scope(scope_id)

                self.replace_inner(inner_node, nodes)

                node.scope_id = None
                self.scopes.remove_scope(scope_id)

                self.leave_scope()

    def remove_nodes(self, nodes: list[VNode], gen_muts: bool):
        for node in nodes:
            match node:
                case VString() as node:
                    if element_id := node.id:
                        self.scopes.remove_node(element_id)
                        node.id = None

                        if gen_muts:
                            self.mutations.append(Remove(element_id))

                case VElement() as node:
                    element_id = cast(ElementId, node.id)

                    if gen_muts:
                        self.mutations.append(Remove(element_id))

                    self.scopes.remove_node(element_id)
                    node.id = None

                    self.remove_nodes(node.children, False)

                case VPlaceholder() as node:
                    element_id = cast(ElementId, node.id)
                    self.scopes.remove_node(element_id)
                    node.id = None

                    if gen_muts:
                        self.mutations.append(Remove(element_id))

                case VComponent() as node:
                    scope_id = node.scope_id
                    assert scope_id is not None

                    scope = self.scopes.get_scope(scope_id)
                    self.enter_scope(scope_id)

                    root = scope.fin_frame()
                    self.remove_nodes([root], gen_muts)
                    node.scope_id = None

                    self.scopes.remove_scope(scope_id)

                    self.leave_scope()

    def create_string_node(self, node: VString, nodes: list[ElementId]):
        element_id = self.scopes.reserve_node(node)
        node.id = element_id
        self.mutations.append(CreateTextNode(element_id, node.data))
        nodes.append(element_id)

    def create_element_node(self, parent_id: ElementId, node: VElement, nodes: list[ElementId]):
        node.parent_id = parent_id
        element_id = self.scopes.reserve_node(node)
        node.id = element_id

        self.mutations.append(CreateElement(element_id, node.tag))

        scope_id = self.current_scope()

        for listener in node.listeners:
            self.mutations.append(NewEventListener(listener.name, scope_id, element_id))

        for key, value in node.attributes.items():
            self.mutations.append(SetAttribute(element_id, key, value))

        if children := node.children:
            self.create_and_append_children(element_id, children)

        nodes.append(element_id)

    def create_placeholder_node(self, node: VPlaceholder):
        element_id = self.scopes.reserve_node(node)
        node.id = element_id
        self.mutations.append(CreatePlaceholder(element_id))

    def create_componet_node(self, parent_id: ElementId, node: VComponent, nodes: list[ElementId]):
        parent_scope = self.current_scope()

        if not (scope_id := node.scope_id):
            scope_id = self.scopes.new_scope(parent_scope, parent_id)
            scope = self.scopes.get_scope(scope_id)
            scope.component = node.func
            node.scope_id = scope_id

        self.enter_scope(scope_id)

        self.scopes.run_scope(scope_id)
        self.mutations.mark_dirty(scope_id)
        next_node = self.scopes.get_scope(scope_id).fin_frame()
        self.create_node(parent_id, next_node, nodes)

        self.leave_scope()

    def create_and_append_children(self, parent_id: ElementId, nodes: list[VNode]):
        children_nodes: list[ElementId] = []
        self.create_children(parent_id, nodes, children_nodes)
        self.mutations.append(AppendChildren(parent_id, children_nodes))

    def create_children(self, parent_id: ElementId, nodes: list[VNode], children_nodes: list[ElementId], ):
        for node in nodes:
            self.create_node(parent_id, node, children_nodes)

    def create_and_insert_after(self, parent_id: ElementId, nodes: list[VNode], after: VNode):
        assert after.id

        created: list[ElementId] = []
        self.create_children(parent_id, nodes, created)
        self.mutations.append(InsertAfter(after.id, created))

    def current_scope(self) -> ScopeId:
        return self.scope_stack[-1]

    def enter_scope(self, scope_id: ScopeId):
        self.scope_stack.append(scope_id)

    def leave_scope(self):
        del self.scope_stack[-1]
