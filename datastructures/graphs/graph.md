# Graph (`graph.py`)

Adjacency-matrix representation of a directed/weighted graph.

## Implementation
- `Graph(num_nodes=6, adjacency_matrix=None)`: Uses the provided `adjacency_matrix`, or generates a random `num_nodes × num_nodes` binary (`0`/`1`) adjacency matrix when none is passed.
- `get_adjacency_matrix()`: Returns the underlying `list[list[int]]`.
- `to_string()`: Prints the adjacency matrix.

## Complexity
- Initialization (random): $O(V^2)$ time.
- Space: $O(V^2)$ for the adjacency matrix.
