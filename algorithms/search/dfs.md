# Depth-First Search (`dfs.py`)

Iterative depth-first search finding a path from `source` to `target` in an adjacency-matrix `Graph`.

## Implementation
- `dfs(graph, source, target, no_repeats=True)`:
  - Uses a LIFO `deque[Node]` stack (`pop()`) and tracks visited vertices when `no_repeats=True`.
  - Expands neighbors with `g[current.val][node] >= 1`, recording parent pointers on each `Node`.
  - Reconstructs and returns the `source → target` path via `get_parent()` once `target` is popped, or returns `None` if unreachable.

## Complexity
- Time: $O(V^2)$ due to scanning each row of the adjacency matrix.
- Space: $O(V)$ for the stack, visited list, and parent chain.
