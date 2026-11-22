from typing import Any, Generic, Protocol, TypeVar, cast


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


class MinHeap(Generic[T]):
    def __init__(self) -> None:
        self.min_heap: list[T] = []

    def _sift_up(self, idx: int) -> None:
        while idx > 0 and self.min_heap[(idx - 1) // 2] > self.min_heap[idx]:
            parent = (idx - 1) // 2
            self.min_heap[idx], self.min_heap[parent] = (
                self.min_heap[parent],
                self.min_heap[idx],
            )
            idx = parent

    def _sift_down(self, idx: int) -> None:
        size = len(self.min_heap)
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2
            smallest = idx

            if left < size and self.min_heap[left] < self.min_heap[smallest]:
                smallest = left
            if right < size and self.min_heap[right] < self.min_heap[smallest]:
                smallest = right
            if smallest != idx:
                self.min_heap[smallest], self.min_heap[idx] = (
                    self.min_heap[idx],
                    self.min_heap[smallest],
                )
                idx = smallest
            else:
                break

    def heap_push(self, value: T) -> None:
        self.min_heap.append(value)
        self._sift_up(len(self.min_heap) - 1)

    def heap_delete(self, value: T) -> None:
        if not self.min_heap:
            return

        i = len(self.min_heap) - 1
        while i >= 0 and self.min_heap[i] != value:
            i -= 1

        if i < 0:
            return

        self.min_heap[i] = self.min_heap[-1]
        self.min_heap.pop()

        if i < len(self.min_heap):
            if i > 0 and self.min_heap[i] < self.min_heap[(i - 1) // 2]:
                self._sift_up(i)
            else:
                self._sift_down(i)

    def heap_pop(self) -> T:
        root = self.min_heap[0]
        last = self.min_heap.pop()
        if self.min_heap:
            self.min_heap[0] = last
            self._sift_down(0)
        return root

    def heap_search(self, value: Any) -> bool:
        for element in self.min_heap:
            if element == value:
                return True
            if isinstance(element, tuple):
                items = cast(tuple[Any, ...], element)
                if len(items) > 1 and items[1] == value:
                    return True
        return False

    def is_empty(self) -> bool:
        return len(self.min_heap) == 0

    def heap_print(self) -> None:
        print(self.min_heap)


# Testing
# test_heap = MinHeap()
# test_heap.heap_push(5)
# test_heap.heap_push(3)
# test_heap.heap_push(2)
# test_heap.heap_push(12)
# test_heap.heap_push(13)
# test_heap.heap_print()
# print(test_heap.heap_pop())
# test_heap.heap_push(9)
# test_heap.heap_print()
# test_heap.heap_delete(2)
# test_heap.heap_print()
# print(test_heap.heap_pop())

# test_heap = MinHeap()
# test_heap.heap_push((13, 5))
# test_heap.heap_push((1, 4))
# test_heap.heap_push((3, 7))
# test_heap.heap_push((10, 2))
# test_heap.heap_push((9, 1))
# test_heap.heap_print()
# print(test_heap.heap_pop())
# test_heap.heap_delete((1, 4))
# test_heap.heap_print()
