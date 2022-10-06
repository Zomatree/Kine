from typing_extensions import reveal_type
from .core import VElement, VNode, VString
from .scope import ElementId

class Modification:
    def __init__(self, id: ElementId):
        self.id = id

class SetText(Modification):
    def __init__(self, id: ElementId, text: str):
        super().__init__(id)
        self.text = text

class ReplaceNode(Modification):
    def __init__(self, id: ElementId, node: VNode):
        super().__init__(id)
        self.node = node

RemoveNode = Modification

class CreateElement(Modification):
    def __init__(self, node: VElement):
        super().__init__(node.id)
        self.node = node

class CreateString(Modification):
    def __init__(self, node: VString):
        super().__init__(node.id)
        self.node = node

class Diff:
    def __init__(self, initial: VNode):
        self.current = initial

    def diff(self, next: VNode) -> list[Modification]:
        mutations: list[Modification] = []
        reveal_type((self.current, next))

        match self.current, next:
            case VString() as before, VString() as after:
                self.diff_string_nodes(mutations, before, after)

            case VElement() as before, VElement() as after:
                self.diff_element_nodes(mutations, before, after)

            case VElement() | VString() as before, None:
                mutations.append(RemoveNode(before.id))

            case None, VElement() as after:
                mutations.append(CreateElement(after))

            case None, VString() as after:
                mutations.append(CreateString(after))

            case (VString() | VElement()) as before, (VString() | VElement()) as after:
                mutations.append(ReplaceNode(before.id, after))

            case None, None:
                pass

        self.current = next
        return mutations

    def diff_string_nodes(self, mutations: list[Modification], before: VString, after: VString):
        if before == after:
            return

        mutations.append(SetText(before.id, str(after)))

    def diff_element_nodes(self, mutations: list[Modification], before: VElement, after: VElement):
        # fast way to check if they are the same without needing to compare every child value
        if id(before) == id(after):
            return

        if before.tag != after.tag:
            mutations.append(ReplaceNode(before.id, after))
            return

