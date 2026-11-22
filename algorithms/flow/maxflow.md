# Maximum Flow — Edmonds–Karp (`maxflow.py`)

Computes the maximum `source → sink` flow in a directed capacitated network using Ford–Fulkerson with BFS shortest augmenting paths (Edmonds–Karp).

## Implementation
- `create_residual_graph(flow_g, o_g)`: Computes residual capacities `o_g[i][j] - flow_g[i][j]` using skew-symmetric net flows.
- `get_min_capacity_along_path(aug_path, g)`: Finds the bottleneck capacity along an augmenting path.
- `push_flow_on_graph(additional_flow, g, aug_path)`: Adds `additional_flow` along forward edges and subtracts it along reverse edges.
- `max_flow(network, source, sink)`: Repeatedly runs `bfs` on the residual graph, pushes bottleneck flow along each augmenting path, and stops when no `source → sink` path remains.

## Complexity
- Time: $O(V E^2)$ with adjacency lists; $O(V^3 E)$ here due to $O(V^2)$ matrix residual rebuilds and BFS per augmentation.
- Space: $O(V^2)$ for the flow and residual matrices.
