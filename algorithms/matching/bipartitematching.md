# Maximum Bipartite Matching (`bipartitematching.py`)

Reduces maximum-cardinality bipartite matching (on a balanced bipartite adjacency matrix) to unit-capacity maximum flow.

## Implementation
- `expand_graph_to_network(o_g)`: Pads the adjacency matrix with a super-source (index `0`) and super-sink (last index) using NumPy, connecting the source to the left partition and the right partition to the sink with capacity `1` (and clearing self-loops and cross-partition source/sink edges).
- `bipartite_matching(graph)`: Converts the bipartite graph into a flow network and returns the max-flow value from `max_flow`.

## Complexity
- Time: Dominated by `max_flow` on unit-capacity edges ($O(V^3)$ with the matrix-based BFS flow implementation).
- Space: $O(V^2)$.
