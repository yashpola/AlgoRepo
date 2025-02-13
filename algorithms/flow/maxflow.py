import sys

sys.path.insert(0, "/Users/yashpola/Repositories/AlgoRepo/datastructures/graphs")
sys.path.insert(0, "/Users/yashpola/Repositories/AlgoRepo/algorithms/search")

from bfs import bfs
from graph import Graph

from math import inf


def create_residual_graph(
    flow_g: list[list[int]], o_g: list[list[int]]
) -> list[list[int]]:
    residual_graph = [[0] * len(o_g[0]) for _ in range(len(o_g))]

    for i in range(len(o_g)):
        for j in range(len(o_g[0])):
            if o_g[i][j] > 0:
                residual_graph[i][j] = o_g[i][j] - flow_g[i][j]
                residual_graph[j][i] = flow_g[i][j]

    return residual_graph


def get_min_capacity_along_path(aug_path: list[int], g: list[list[int]]) -> int:
    min_capacity = inf
    for i in range(len(aug_path) - 1):
        min_capacity = min(min_capacity, g[aug_path[i]][aug_path[i + 1]])
    return min_capacity


def push_flow_on_graph(
    additional_flow: int, g: list[list[int]], aug_path: list[int]
) -> Graph:
    for i in range(len(aug_path) - 1):
        g[aug_path[i]][aug_path[i + 1]] += additional_flow
        g[aug_path[i + 1]][aug_path[i]] -= additional_flow
    return g


def max_flow(
    network: list[list[int]], source: int, sink: int
) -> tuple[int, list[list[int]]]:
    max_flow = 0

    current_flow = [[0] * len(network[0]) for _ in range(len(network))]
    g_f = create_residual_graph(current_flow, network)
    aug_path = bfs(Graph(num_nodes=len(g_f), adjacency_matrix=g_f), source, sink)

    while aug_path is not None:
        additional_flow = get_min_capacity_along_path(aug_path, g_f)
        max_flow += additional_flow
        current_flow = push_flow_on_graph(additional_flow, current_flow, aug_path)
        g_f = create_residual_graph(current_flow, network)
        aug_path = bfs(Graph(num_nodes=len(g_f), adjacency_matrix=g_f), source, sink)

    return max_flow, current_flow


# Test 1
def test_1():
    flow_value, flow_network = max_flow(
        [
            [0, 4, 2, 0, 0, 0],
            [0, 0, 0, 3, 0, 0],
            [0, 3, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 2],
            [0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0],
        ],
        0,
        5,
    )
    print(flow_value)
    print(flow_network)


# Test 2
def test_2():
    flow_value, _ = max_flow(
        [
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],
        0,
        6,
    )
    print(flow_value)
