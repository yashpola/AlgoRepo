# Chan's Convex Hull Algorithm (`chan.py`)

Output-sensitive 2D convex hull algorithm that combines Andrew's monotone chain with Jarvis march and tangent binary search.

## Implementation
- `Point`: Frozen dataclass `(x, y)` for hashability and deduplication.
- `cross(o, a, b)`, `dist2(a, b)`, `is_better(p, a, b)`: 2D cross-product orientation test (`< 0` = clockwise / further right) with furthest-distance tie-breaking for collinear points.
- `monotone_chain(points)`: Builds a counter-clockwise convex hull of a small group in $O(m \log m)$ time by sweeping left-to-right (lower hull) and right-to-left (upper hull).
- `right_tangent(H, p)`: Circular binary search on a CCW mini-hull `H` to find the most clockwise vertex from `p` in $O(\log m)$ time.
- `conditional_hull(points, h_star)`: Partitions `points` into $\lceil n / h^* \rceil$ mini-hulls of size $\le h^*$, then runs up to $h^*$ steps of Jarvis march across their right tangents; returns `(False, [])` if the hull does not close in $h^*$ steps.
- `chan_convex_hull(points)`: Deduplicates input and repeatedly squares the guess $h^* = 4, 16, 256, \dots$ (clamped to $n$) until `conditional_hull` succeeds.

## Complexity
- Time: $O(n \log h)$, where $h$ is the number of vertices on the convex hull.
- Space: $O(n)$.
