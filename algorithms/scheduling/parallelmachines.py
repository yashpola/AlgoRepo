def parallemachines(start_times: list[int], end_times: list[int]) -> int:
    starts = sorted(start_times)
    ends = sorted(end_times)
    i = j = active = max_active = 0
    while i < len(starts) and j < len(ends):
        if starts[i] < ends[j]:
            active += 1
            max_active = max(active, max_active)
            i += 1
            continue
        active -= 1
        j += 1

    return max_active

print(parallemachines([1, 2, 7, 9], [4, 5, 9, 11]))
print(parallemachines([], []))