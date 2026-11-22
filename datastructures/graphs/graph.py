import random


class Graph:

    def __init__(
        self, num_nodes: int = 6, adjacency_matrix: list[list[int]] | None = None
    ) -> None:
        if not adjacency_matrix:
            self.__adjacency_matrix: list[list[int]] = [
                [0] * num_nodes for _ in range(num_nodes)
            ]
            for i in range(num_nodes):
                for j in range(num_nodes):
                    self.__adjacency_matrix[i][j] = random.randint(0, 1)
        else:
            self.__adjacency_matrix = adjacency_matrix

    def get_adjacency_matrix(self) -> list[list[int]]:
        return self.__adjacency_matrix

    def to_string(self) -> None:
        print(self.__adjacency_matrix)
