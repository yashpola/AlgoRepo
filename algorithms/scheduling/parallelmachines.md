# Parallel Machines / Interval Partitioning (`parallelmachines.py`)

Sweep-line two-pointer algorithm that finds the minimum number of parallel machines needed to schedule all intervals without overlap (equivalent to maximum concurrent intervals).

## Implementation
- `parallemachines(start_times, end_times)`:
  - Sorts copies of `start_times` and `end_times`.
  - Advances two pointers `i` and `j`: increments `active` when `starts[i] < ends[j]` (updating `max_active`), and decrements `active` otherwise (a job finishes at or before the next starts).

## Complexity
- Time: $O(n \log n)$ for sorting, $O(n)$ for the sweep.
- Space: $O(n)$ for the sorted copies.
