from typing import ClassVar, Mapping, Self, TypeVar, TypedDict, Any
from pkg_resources import Distribution, Requirement

def get_installed_distributions(local_only: bool = False, user_only: bool = False) -> list[Distribution]:
    ...

class Package:
    project_name: str
    key: str

    def __init__(self, obj: Distribution) -> None:
        ...

    def render_as_root(self, frozen: bool) -> str:
        ...

    def render_as_branch(self, frozen: bool) -> str:
        ...

    def render(self, parent: Package | None = None, frozen: bool = False) -> str:
        ...

    @staticmethod
    def frozen_repr(obj: Distribution) -> str:
        ...

class DistPackageDict(TypedDict):
    key: str
    package_name: str
    project_name: str
    installed_version: str

class DistPackage(Package):
    def __init__(self, obj: Distribution, req: ReqPackage | None = None) -> None:
        ...

    def as_requirement(self) -> str:
        ...

    def as_parent_of(self, req: ReqPackage) -> Self:
        ...

    def as_dict(self) -> DistPackageDict:
        ...

class ReqPackageDict(TypedDict):
    key: str
    package_name: str
    installed_version: str
    required_version: str

class ReqPackage(Package):
    UNKNOWN_VERSION: ClassVar[str]

    def __init__(self, obj: Requirement, dist: Distribution | None) -> None:
        ...

    @property
    def version_spec(self) -> str:
        ...

    @property
    def installed_version(self) -> str:
        ...

    @property
    def is_missing(self) -> bool:
        ...

    def is_conflicting(self) -> bool:
        ...

    def as_dict(self) -> ReqPackageDict:
        ...

K = TypeVar("K", default=DistPackage)
V = TypeVar("V", default=ReqPackage)

class PackageDAG(Mapping[K, list[V]]):
    def __init__(self, m: dict[K, list[V]]) -> None:
        ...

    def get_node_as_parent(self, node_key: str) -> K | None:
        ...

    def get_children(self, node_key: str) -> list[ReqPackage]:
        ...

    @classmethod
    def from_pkgs(cls, pkgs: list[Distribution]) -> Self:
        ...

    def filter(self, include: list[str], exclude: list[str]) -> Self:
        ...

    def reverse(self) -> ReversedPackageDAG[V, K]:
        ...

    def sort(self) -> Self:
        ...

class ReversedPackageDAG(PackageDAG[V, K]):
    def reverse(self) -> PackageDAG[K, V]:
        ...

def render_text(tree: PackageDAG[Any, Any], list_all: bool = True, frozen: bool = False) -> None:
    ...

def render_json(tree: PackageDAG[Any, Any], indent: int) -> str:
    ...

def render_json_tree(tree: PackageDAG[Any, Any], indent: int) -> str:
    ...

def render_mermaid(tree: PackageDAG[Any, Any]) -> str:
    ...

def dump_graphviz(tree: PackageDAG[Any, Any], output_foprmat: str = "dot", is_reverse: bool = False) -> str | bytes:
    ...

def print_graphviz(dump_output: str | bytes) -> None:
    ...

def conflicting_deps(tree: PackageDAG[K, V]) -> dict[K, list[V]]:
    ...

def render_conflicts_text(conflicts: dict[Any, list[Any]]) -> None:
    ...

def cyclic_deps(tree: PackageDAG[K, V]) -> list[tuple[K, V, list[V]]]:
    ...

def render_cycles_text(cycles: list[tuple[Any, V, list[V]]]) -> None:
    ...
