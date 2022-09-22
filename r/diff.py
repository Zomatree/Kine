from .r import VComponent, VElement, VNode, VString
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

class Diff:
    def __init__(self, initial: VNode):
        self.current = initial

    def diff(self, next: VNode) -> list[Modification]:
        mutations: list[Modification] = []

        match self.current, next:
            case VString() as before, VString() as after:
                self.diff_string_nodes(mutations, before, after)

            case VElement() as before, VElement() as after:
                self.diff_element_nodes(mutations, before, after)

            case VString() | VComponent() | VElement() as before, VString() | VComponent() | VElement() as after:
                mutations.append(ReplaceNode(before.id, after))

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

        