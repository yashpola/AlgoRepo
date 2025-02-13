from collections import deque

import sys

sys.path.insert(0, "/Users/yashpola/Repositories/AlgoRepo/datastructures/graphs")

from graph import Graph
from node import Node


def bfs(graph: Graph, source: int, target: int, no_repeats=True) -> list[int] | None:
    g = graph.get_adjacency_matrix()
    path = []
    frontier = deque()
    visited = []

    src = Node(source)
    frontier.append(src)
    visited.append(src.val)
    while len(frontier) != 0:
        current = frontier.popleft()
        if current.val == target:
            while current != None:
                path.append(current.val)
                current = current.get_parent()
            path.reverse()
            return path

        neighbors = [node for node in range(len(g)) if g[current.val][node] >= 1]
        for neighbor in neighbors:
            if no_repeats:
                if neighbor not in visited:
                    next = Node(neighbor, current)
                    visited.append(neighbor)
                    frontier.append(next)
                continue
            next = Node(neighbor, current)
            frontier.append(next)
    return None


def main():
    # Graph (V, E) with uniform edge cost of 1 if edge (u, v) in E
    graph = Graph(
        [
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ],
        False,
    )
    print(bfs(graph, 0, 5))
