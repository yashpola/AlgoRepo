import random


class Graph:

    def __init__(self, adjacency_matrix=None, random_graph=True):
        if random_graph:
            self.__adjacency_matrix = [[0] * 6 for _ in range(6)]
            for i in range(6):
                for j in range(6):
                    self.__adjacency_matrix[i][j] = round(random.randint(0, 1))
        else:
            self.__adjacency_matrix = adjacency_matrix

    def get_adjacency_matrix(self):
        return self.__adjacency_matrix

    def to_string(self):
        print(self.__adjacency_matrix)
