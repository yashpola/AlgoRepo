import copy
import random


def pick_random_edge(
    adj_matrix: list[list[int]], active_nodes: list[int]
) -> tuple[int, int] | None:
    """Pick a random edge (u, v) from the adjacency matrix where u and v are active."""
    edges: list[tuple[int, int]] = []
    weights: list[int] = []
    for idx, u in enumerate(active_nodes):
        for v in active_nodes[idx + 1 :]:
            if adj_matrix[u][v] > 0:
                edges.append((u, v))
                weights.append(adj_matrix[u][v])

    if not edges:
        return None
    return random.choices(edges, weights=weights, k=1)[0]


def contract_edge(
    adj_matrix: list[list[int]], u: int, v: int, active_nodes: set[int]
) -> None:
    """Contracts edge (u, v) by merging v into u and removing v."""
    for w in active_nodes:
        if w != u and w != v:
            # Merge v's edges into u
            adj_matrix[u][w] += adj_matrix[v][w]
            adj_matrix[w][u] = adj_matrix[u][w]  # Maintain symmetry

    # Mark v as deleted (invalidate all its edges)
    active_nodes.remove(v)
    for w in range(len(adj_matrix)):
        adj_matrix[v][w] = 0
        adj_matrix[w][v] = 0


def karger_min_cut(adj_matrix: list[list[int]]) -> int:
    """Runs Karger's Min Cut algorithm on an adjacency matrix."""
    n = len(adj_matrix)
    if n < 2:
        return 0

    min_cut: int | None = None

    for _ in range(n**2):  # Run multiple trials to improve accuracy
        adj_copy = copy.deepcopy(adj_matrix)  # Make a deep copy for each trial
        active_nodes = set(range(n))  # Track remaining nodes

        disconnected = False
        while len(active_nodes) > 2:
            edge = pick_random_edge(adj_copy, list(active_nodes))
            if edge is None:
                disconnected = True
                break
            u, v = edge
            contract_edge(adj_copy, u, v, active_nodes)

        if disconnected:
            return 0

        # After contraction, the remaining two nodes should have all cut edges
        remaining_nodes = list(active_nodes)
        u, v = remaining_nodes[0], remaining_nodes[1]
        cut_size = adj_copy[u][v]  # The number of edges in the cut

        if min_cut is None or cut_size < min_cut:
            min_cut = cut_size

    return min_cut if min_cut is not None else 0


# Test 1
def test_1() -> None:
    cut_size = karger_min_cut(
        [[0, 2, 0, 1], [2, 0, 1, 0], [0, 1, 0, 2], [1, 0, 2, 0]]
    )
    print(f"cut size: {cut_size}")
