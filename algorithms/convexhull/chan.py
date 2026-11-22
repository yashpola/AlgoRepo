from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def cross(o: Point, a: Point, b: Point) -> float:
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def dist2(a: Point, b: Point) -> float:
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


def is_better(p: Point, a: Point, b: Point) -> bool:
    c = cross(p, a, b)
    if c < 0:
        return True
    if c > 0:
        return False

    return dist2(p, b) > dist2(p, a)


def monotone_chain(points: list[Point]) -> list[Point]:
    points.sort(key=lambda p: (p.x, p.y))

    if len(points) <= 1:
        return points

    lower: list[Point] = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper: list[Point] = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def right_tangent(H: list[Point], p: Point) -> Point:
    m = len(H)
    if p == H[0]:
        return H[1 % m]

    if m <= 3:
        best = H[0]
        for i in range(1, m):
            if is_better(p, best, H[i]):
                best = H[i]
        return best

    if not is_better(p, H[0], H[1]) and not is_better(p, H[0], H[m - 1]):
        return H[0]

    up_0 = is_better(p, H[0], H[1])
    lo = 0
    hi = m - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        prev = (mid - 1 + m) % m
        after = (mid + 1) % m

        if not is_better(p, H[mid], H[prev]) and not is_better(p, H[mid], H[after]):
            return H[mid]

        up_mid = is_better(p, H[mid], H[after])
        if up_0:
            if not up_mid or not is_better(p, H[0], H[mid]):
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if up_mid or not is_better(p, H[0], H[mid]):
                lo = mid + 1
            else:
                hi = mid - 1

    return H[lo % m]


def conditional_hull(points: list[Point], h_star: int) -> tuple[bool, list[Point]]:
    n = len(points)

    mini_hulls: list[list[Point]] = []
    for i in range(0, n, h_star):
        group = points[i : min(i + h_star, n)]
        mini_hulls.append(monotone_chain(group))

    start = min(points, key=lambda p: (p.y, p.x))
    hull: list[Point] = [start]
    curr = start
    for _ in range(h_star):
        best: Point = curr
        for H in mini_hulls:
            candidate: Point = right_tangent(H, curr)
            if candidate != curr and (best == curr or is_better(curr, best, candidate)):
                best = candidate

        if best == start:
            return (True, hull)

        hull.append(best)
        curr = best

    return (False, [])


def chan_convex_hull(points: list[Point]) -> list[Point]:
    points = list(set(points))
    if len(points) <= 1:
        return points

    h_star = 2
    while True:
        h_star = min(h_star**2, len(points))
        success, hull = conditional_hull(points, h_star)
        if success:
            return hull
        if h_star == len(points):
            raise RuntimeError("Failed to compute convex hull")


if __name__ == "__main__":
    # 1. Square with interior points
    pts1 = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4), Point(2, 2), Point(1, 3), Point(3, 1)]
    expected1 = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]
    assert chan_convex_hull(pts1) == expected1

    # 2. Rectangle with collinear edge points and duplicates
    pts2 = [Point(0, 0), Point(2, 0), Point(4, 0), Point(4, 2), Point(2, 2), Point(0, 2), Point(0, 0), Point(2, 1)]
    expected2 = [Point(0, 0), Point(4, 0), Point(4, 2), Point(0, 2)]
    assert chan_convex_hull(pts2) == expected2

    # 3. Pentagon with interior points (h = 5, exercises h* = 4 -> 16)
    pts3 = [Point(0, 2), Point(2, 0), Point(5, 1), Point(6, 4), Point(3, 6), Point(2, 3), Point(3, 3), Point(4, 2)]
    expected3 = [Point(2, 0), Point(5, 1), Point(6, 4), Point(3, 6), Point(0, 2)]
    assert chan_convex_hull(pts3) == expected3

    print("All test cases passed!")
