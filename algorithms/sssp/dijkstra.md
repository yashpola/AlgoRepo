# Dijkstra's Shortest Path (`dijkstra.py`)

Single-source shortest path algorithm for graphs with non-negative edge weights, using the repo's custom `MinHeap`.

## Implementation
- `dijkstra(graph, distances, src, dest)`:
  - Takes a 1-indexed adjacency list `graph` and weight matrix `distances` (`inf` for missing edges).
  - Initializes `shortest_distances` (`0` for `src`, `inf` for others) and pushes `(distance, node)` entries into `MinHeap[tuple[float, int]]`.
  - Repeatedly pops the minimum-distance entry, skips stale heap entries (`distance > shortest_distances[node]`), relaxes outgoing edges, and pushes improved distances.
  - Returns `shortest_distances[dest]`.

## Complexity
- Time: $O((V + E) \log V)$ using the binary min-heap.
- Space: $O(V + E)$ for distance tracking and heap entries (plus $O(V^2)$ for the input `distances` matrix).
