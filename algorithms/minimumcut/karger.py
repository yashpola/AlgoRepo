import sys

import random


# return graph with new merged node pair(s)
def create_contracted_graph(o_g: list[list[int]], edge: tuple[int]) -> list[list[int]]:
    c_g = [[0] * (len(o_g[0]) - 1) for _ in range(len(o_g) - 1)]

    u, v = edge

    # merge v into u
    for i in range(len(o_g) - 1):
        for j in range(len(o_g[0]) - 1):
            if j not in edge:
                c_g[i][j] += o_g[i][j]
                c_g[j][i] = c_g[i][j]
    c_g[min(edge)][min(edge)] = -1

    return c_g


# util function to pick a random edge from the list of edges
def pick_random_edge(c_g: list[list[int]]) -> tuple[int]:
    i: int = random.randint(0, len(c_g[0]) - 1)
    adjacent_nodes_excluding_i: list[int] = []
    for j in range(len(c_g[0])):
        if c_g[i][j] != -1:
            adjacent_nodes_excluding_i.append(j)
    j: int = adjacent_nodes_excluding_i[
        random.randint(0, len(adjacent_nodes_excluding_i) - 1)
    ]
    return i, j


# construct the minimum cut
def karger(graph: list[list[int]]) -> tuple[int, list[tuple[int]]]:

    contracted_graph: list[list[int]] = graph
    while len(contracted_graph[0]) > 2:
        i, j = pick_random_edge(contracted_graph)
        contracted_graph = create_contracted_graph(contracted_graph, (i, j))

    cut_size: int = 0
    cut_edges: list[tuple[int]] = []
    for i in range(len(contracted_graph)):
        for j in range(len(contracted_graph[0])):
            if contracted_graph[i][j] != -1 and (
                (i, j) not in cut_edges or (j, i) not in cut_edges
            ):
                cut_size += contracted_graph[i][j]
                cut_edges += [(i, j) for _ in range(contracted_graph[i][j])]

    return cut_size, cut_edges


# Test 1
def test_1():
    try:
        cut_size, cut_edges = karger(
            [[0, 2, 0, 0], [2, 0, 1, 0], [0, 1, 0, 2], [1, 0, 2, 0]],
        )
        print(f"cut size: {cut_size}")
        print(f"cut_edges: {cut_edges}")
    except Exception as e:
        print(e)


# test_1()

import random
import copy


def pick_random_edge(adj_matrix, active_nodes):
    """Pick a random edge (u, v) from the adjacency matrix where u and v are active."""
    while True:
        u = random.choice(active_nodes)  # Randomly pick a node from remaining nodes
        neighbors = [v for v in active_nodes if adj_matrix[u][v] > 0 and u != v]
        if neighbors:
            v = random.choice(neighbors)
            return u, v


def contract_edge(adj_matrix, u, v, active_nodes):
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


def karger_min_cut(adj_matrix):
    """Runs Karger's Min Cut algorithm on an adjacency matrix."""
    n = len(adj_matrix)
    min_cut = float("inf")

    for _ in range(n**2):  # Run multiple trials to improve accuracy
        adj_copy = copy.deepcopy(adj_matrix)  # Make a deep copy for each trial
        active_nodes = set(range(n))  # Track remaining nodes

        while len(active_nodes) > 2:
            u, v = pick_random_edge(adj_copy, list(active_nodes))
            contract_edge(adj_copy, u, v, active_nodes)

        # After contraction, the remaining two nodes should have all cut edges
        remaining_nodes = list(active_nodes)
        u, v = remaining_nodes[0], remaining_nodes[1]
        cut_size = adj_copy[u][v]  # The number of edges in the cut

        min_cut = min(min_cut, cut_size)

    return min_cut


# Example usage
graph = {0: {1: 3, 2: 1}, 1: {0: 3, 2: 2, 3: 4}, 2: {0: 1, 1: 2, 3: 2}, 3: {1: 4, 2: 2}}

# min_cut_size, min_cut_edges = karger(graph)
# print("Min Cut Size:", min_cut_size)
# print("Min Cut Edges:", min_cut_edges)
