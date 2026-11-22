from typing import Any


def print_matrix(grid: list[list[Any]]) -> None:
    for row in grid:
        print(row)


# Levenshtein distance - substitutions allowed and cost 2 units.
def minimumEditDistance(source: str, target: str) -> tuple[int, list[str]]:
    m, n = len(source), len(target)

    dpTable: list[list[tuple[int, list[str]]]] = [
        [(0, []) for _ in range(n + 1)] for _ in range(m + 1)
    ]

    for i in range(1, m + 1):
        dpTable[i][0] = (i, ["D"])
    for j in range(1, n + 1):
        dpTable[0][j] = (j, ["I"])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            delete_cost = dpTable[i - 1][j][0] + 1
            insert_cost = dpTable[i][j - 1][0] + 1
            sub_cost = dpTable[i - 1][j - 1][0] + (
                0 if source[i - 1] == target[j - 1] else 2
            )

            min_cost = min(delete_cost, insert_cost, sub_cost)
            dirs: list[str] = []
            if delete_cost == min_cost:
                dirs.append("D")
            if insert_cost == min_cost:
                dirs.append("I")
            if sub_cost == min_cost:
                dirs.append("M" if source[i - 1] == target[j - 1] else "S")

            dpTable[i][j] = (min_cost, dirs)

    path: list[str] = []
    i, j = m, n
    while dpTable[i][j][1]:
        directions = dpTable[i][j][1]
        move = directions[0]
        if move == "M":
            i -= 1
            j -= 1
        elif move == "S":
            path.append(f"Substitution from {source[i - 1]} to {target[j - 1]}")
            i -= 1
            j -= 1
        elif move == "D":
            path.append(f"Deletion of {source[i - 1]}")
            i -= 1
        elif move == "I":
            path.append(f"Insertion of {target[j - 1]}")
            j -= 1

    path.reverse()
    return dpTable[m][n][0], path


# print(minimumEditDistance("abcd", "bcfe"))
print(minimumEditDistance("cheap", "help"))
# print(minimumEditDistance("intention", "execution"))
