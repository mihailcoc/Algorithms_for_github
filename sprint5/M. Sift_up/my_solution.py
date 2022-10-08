def sift_up(heap: set, idx: int) -> int:
    while idx > 1 and heap[idx] > heap[idx // 2]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx //= 2
    return idx
