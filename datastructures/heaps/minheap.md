# MinHeap (`minheap.py`)

Generic binary min-heap (`MinHeap[T]`) backed by a Python list, supporting any comparable type (including `(priority, node)` tuples).

## Implementation
- `_sift_up(idx)` / `_sift_down(idx)`: Restore the min-heap invariant using 0-based parent `(i - 1) // 2` and child `2i + 1`, `2i + 2` indices.
- `heap_push(value)`: Appends `value` and sifts up.
- `heap_pop()`: Removes and returns the minimum element at index `0`, moving the last element to the root and sifting down.
- `heap_delete(value)`: Linearly locates `value`, replaces it with the last element, and sifts up or down to restore the heap property.
- `heap_search(value)`: Linear scan matching either the element directly or `element[1]` for tuple entries.
- `is_empty()` / `heap_print()`: Emptiness check and debug printing.

## Complexity
- `heap_push`, `heap_pop`: $O(\log n)$ time.
- `heap_delete`, `heap_search`: $O(n)$ time.
- Space: $O(n)$.
