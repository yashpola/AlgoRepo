from collections.abc import Sequence
from math import inf
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from datastructures.heaps.minheap import MinHeap


def dijkstra(
    graph: dict[int, list[int]],
    distances: Sequence[Sequence[float]],
    src: int,
    dest: int,
) -> float:
    shortest_distances: dict[int, float] = {}
    unvisited_nodes: MinHeap[tuple[float, int]] = MinHeap()

    for node in graph:
        if node == src:
            shortest_distances[node] = 0
            unvisited_nodes.heap_push((0, node))
        else:
            shortest_distances[node] = inf
            unvisited_nodes.heap_push((inf, node))

    while not unvisited_nodes.is_empty():
        distance_to_closest_node, closest_node = unvisited_nodes.heap_pop()
        if distance_to_closest_node > shortest_distances[closest_node]:
            continue

        for neighbor in graph[closest_node]:
            weight = distances[closest_node - 1][neighbor - 1]
            if weight == inf:
                continue

            if shortest_distances[closest_node] + weight < shortest_distances[neighbor]:
                shortest_distances[neighbor] = shortest_distances[closest_node] + weight
                unvisited_nodes.heap_push((shortest_distances[neighbor], neighbor))

    return shortest_distances[dest]


print(dijkstra(
    {1: [2, 6], 2: [4], 3: [1], 4: [6, 7], 5: [7], 6: [3, 5], 7: []}, 
    [
        [0, 1, inf, inf, inf, 3, inf], 
        [inf, 0, inf, 4, inf, inf, inf], 
        [1, inf, 0, inf, inf, inf, inf],
        [inf, inf, inf, 0, inf, 2, inf], 
        [inf, inf, inf, inf, 0, inf, 1],
        [inf, inf, 1, inf, 1, 0, inf],
        [inf, inf, inf, inf, inf, inf, 0]
    ], 
    1, 
    7))

print(dijkstra(
    {1: [2, 5], 2: [1, 3, 5], 3: [3, 4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}, 
    [
        [0, 7, inf, inf, 1], 
        [7, 0, 3, inf, 8], 
        [inf, 3, 0, 4, 2],
        [inf, inf, 4, 0, 7], 
        [1, 8, 2, 7, 0],
    ], 
    1, 
    4))
    
    
    