import sys
import numpy as np

sys.path.insert(0, "/Users/yashpola/Repositories/AlgoRepo/algorithms/flow")

sys.path.insert(0, "/Users/yashpola/Repositories/AlgoRepo/algorithms/minimumcut")

from maxflow import max_flow


def expand_graph_to_network(o_g: list[list[int]]) -> list[list[int]]:
    # add source and sink. no flow out of sink, no flow into source
    ndarray = np.pad(
        np.array(o_g),
        1,
        constant_values=((1, 0), (0, 1)),
    )

    # src has no self-loop
    ndarray[0, ndarray.shape[0] - 1] = 0

    midpoint = ndarray.shape[0] // 2
    # left-side nodes of bipartite graph are not adjacent to sink
    ndarray[:midpoint, -1] = 0
    # right-side nodes of bipartite graph are not adjacent to source
    ndarray[0, midpoint:] = 0

    # sink has no self-loop
    ndarray[ndarray.shape[1] - 1, ndarray.shape[1] - 1] = 0

    return ndarray


def bipartite_matching(
    graph: list[list[int]],
) -> list[tuple[int]]:
    network: list[list[int]] = expand_graph_to_network(graph)
    return max_flow(network.tolist(), 0, len(network) - 1)[0]


def test_1():
    max_matching = bipartite_matching(
        [
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    print(max_matching)
