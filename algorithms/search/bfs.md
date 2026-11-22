# Breadth-First Search (`bfs.py`)

Finds a shortest unweighted path (fewest edges) from `source` to `target` in an adjacency-matrix `Graph`.

## Implementation
- `bfs(graph, source, target, no_repeats=True)`:
  - Uses a FIFO `deque[Node]` frontier and tracks visited vertices (when `no_repeats=True`).
  - Explores neighbors where `g[current.val][node] >= 1`, linking each `Node` to its parent.
  - When `target` is dequeued, walks `get_parent()` pointers back to `source` and reverses the list to return the path (or `None` if unreachable).

## Complexity
- Time: $O(V^2)$ due to scanning each row of the adjacency matrix.
- Space: $O(V)$ for the queue, visited list, and parent chain.
