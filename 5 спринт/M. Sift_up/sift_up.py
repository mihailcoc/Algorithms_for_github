class SiftUp:
    def __init__(self):
        self.heap = []

    def make_table(self, N: int):
        for i in range(N):
            self.heap.append((i, 0))
        return self.heap

    def put_idx(heap, idx: int, value: int):
        heap[idx - 1] = value + int(heap[idx - 1])
        value = heap[idx - 1]
        return value

    def sift_up_index(heap: list, index: int) -> int:
        idx = int()
        idx = int(index - 1)
        while int(idx) > 0 and int(heap[int(idx)]) > int(heap[(int(idx) - 1) // 2]):
            heap[int(idx)], heap[(int(idx) - 1) // 2] = heap[(int(idx) - 1) // 2], heap[int(idx)]
            idx = (int(idx) - 1) // 2
            index = int(idx + 1)
        return index


def main():
    heap = SiftUp()
    idx = int()
    heap.make_table(int(input()))
    heap = input().split()
    for i in range(int(input())):
        idx = input().split()
        SiftUp.put_idx(heap, int(idx[0]), int(idx[1]))
        index = SiftUp.sift_up_index(heap, int(idx[0]))
        print(index)
    print(*heap)


if __name__ == '__main__':
    main()