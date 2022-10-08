def sift_down(heap: list, idx: int) -> int:
    left = int()
    left = 2 * idx
    right = int()
    right = left + 1
    while int(left) < int(len(heap)):
        if int(heap[int(idx)]) > int(heap[int(left)]) and (int(right) == int(len(heap)) or int(heap[int(idx)]) > int(heap[int(right)])):
            break
        if int(right) == int(len(heap)) or int(heap[int(left)]) > int(heap[int(right)]):
            heap[int(idx)], heap[int(left)] = heap[int(left)], heap[int(idx)]
            idx = left
        else:
            heap[int(idx)], heap[int(right)] = heap[int(right)], heap[int(idx)]
            idx = right
        left = 2 * idx
        right = left + 1
    return idx
