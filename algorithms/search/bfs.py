from collections import deque
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from datastructures.graphs.graph import Graph
from datastructures.graphs.node import Node


def bfs(
    graph: Graph, source: int, target: int, no_repeats: bool = True
) -> list[int] | None:
    g = graph.get_adjacency_matrix()
    path: list[int] = []
    frontier: deque[Node] = deque()
    visited: list[int] = []

    src = Node(source)
    frontier.append(src)
    visited.append(src.val)
    while len(frontier) != 0:
        current = frontier.popleft()
        if current.val == target:
            node: Node | None = current
            while node is not None:
                path.append(node.val)
                node = node.get_parent()
            path.reverse()
            return path

        neighbors = [node for node in range(len(g)) if g[current.val][node] >= 1]
        for neighbor in neighbors:
            if no_repeats:
                if neighbor not in visited:
                    next_node = Node(neighbor, current)
                    visited.append(neighbor)
                    frontier.append(next_node)
                continue
            next_node = Node(neighbor, current)
            frontier.append(next_node)
    return None


def main() -> None:
    # Graph (V, E) with uniform edge cost of 1 if edge (u, v) in E
    graph = Graph(
        adjacency_matrix=[
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    print(bfs(graph, 0, 5))
