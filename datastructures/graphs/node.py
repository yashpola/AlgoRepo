from __future__ import annotations


class Node:
    def __init__(self, val: int, parent: Node | None = None) -> None:
        self.val = val
        self.parent = parent

    def get_parent(self) -> Node | None:
        return self.parent

    def to_string(self) -> str:
        return f"[Val: {self.val}]"
