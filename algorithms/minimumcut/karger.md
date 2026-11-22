# Karger's Minimum Cut Algorithm (`karger.py`)

Randomized edge-contraction algorithm for finding the global minimum cut of an undirected multigraph given as an adjacency matrix.

## Implementation
- `pick_random_edge(adj_matrix, active_nodes)`: Samples an edge `(u, v)` between active vertices weighted by edge multiplicity (`adj_matrix[u][v]`), returning `None` if the remaining graph is disconnected.
- `contract_edge(adj_matrix, u, v, active_nodes)`: Merges vertex `v` into `u` by summing incident edge counts symmetrically, removes `v` from `active_nodes`, and zeroes out `v`'s row/column.
- `karger_min_cut(adj_matrix)`: Runs $n^2$ independent trials on deep copies of the matrix, contracting until 2 supernodes remain, and returns the smallest cut size observed (`0` if disconnected).

## Complexity
- Time: $O(n^2)$ per contraction trial with an adjacency matrix; $O(n^4)$ across $n^2$ trials.
- Space: $O(n^2)$.
