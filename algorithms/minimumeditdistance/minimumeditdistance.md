# Minimum Edit Distance (`minimumeditdistance.py`)

Bottom-up dynamic programming algorithm computing Levenshtein edit distance (insert = 1, delete = 1, substitute = 2, match = 0) along with an edit sequence.

## Implementation
- `minimumEditDistance(source, target)`:
  - Builds an `(m + 1) × (n + 1)` table `dpTable` storing `(min_cost, directions)` where directions track optimal operations (`"D"`, `"I"`, `"S"`, or `"M"` for character matches).
  - Backtracks from `(m, n)` to `(0, 0)` following the recorded moves, skipping `"M"` matches and reversing the collected edits to return `(distance, path)`.
- `print_matrix(grid)`: Helper to print a 2D table row by row.

## Complexity
- Time: $O(m \cdot n)$ for strings of lengths $m$ and $n$.
- Space: $O(m \cdot n)$.
