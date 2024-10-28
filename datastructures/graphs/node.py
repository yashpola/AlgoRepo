class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent

    def get_parent(self):
        return self.parent

    def to_string(self) -> str:
        print(f"[Val: {self.val}]")
