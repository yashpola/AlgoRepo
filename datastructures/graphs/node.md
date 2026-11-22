# Node (`node.py`)

Lightweight graph search node storing a vertex value and an optional parent pointer for path reconstruction.

## Implementation
- `Node(val, parent=None)`: Stores `val: int` and `parent: Node | None`.
- `get_parent()`: Returns the parent `Node` (or `None` for the start node).
- `to_string()`: Returns `"[Val: <val>]"`.

## Complexity
- All operations: $O(1)$ time and $O(1)$ space per node.
