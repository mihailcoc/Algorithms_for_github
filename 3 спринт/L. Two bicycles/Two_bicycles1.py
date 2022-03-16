class Deque:
    def __init__(self, limit):
        self.queue = [None] * limit
        self.max_n = limit
        self.head = 0
        self.tail = 1
        self.queue_size = 0

    def __getitem__(self, index):
        return self.queue[index]

    def __setitem__(self, index, value):
        self.queue[index] = value

    def is_full(self):
        return self.queue_size == self.max_n

    def index_position(self, index, value):
        return (index + value) % self.max_n

    def push(self, item):
        if self.is_full():
            raise IndexError('error')
        self.head = self.index_position(index=self.head, value=1)
        self.queue[self.head] = item
        self.queue_size += 1

    def size(self):
        return self.queue_size


def binarySearch(arr, x, left, right):
    mid = (left + right) // 2
    middle = int(arr[mid])
    if right <= left:
        if x > middle:
            return -1
        else:
            return mid
    # right = arr.size() - mid
    print(f'левая половина"{left}".')
    print(f'правая половина"{right}".')
    print(f'индекс середины "{mid}"')
    print(f'значение середины "{middle}"')
    middle_minus_1 = int(arr[mid - 1])
    mid1 = mid - 1
    print(f'индекс минус один "{mid1}"')
    print(f'значение середина минус один"{middle_minus_1}"')
    if ((middle == x) and (middle_minus_1 < x)) or (mid == 0):
        return mid
    elif x < middle:  # искомый элемент меньше центрального
                        # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


def main():
    days_length = int(input())
    deque = Deque(days_length)
    parameters = input().split()
    for element in parameters:
        try:
            deque.push(element)
        except ValueError:
            raise TypeError(f' "{element}" - wrong type.')
    bicycle_cost = int(input())
    bicycle_cost2 = bicycle_cost * 2
    result1 = binarySearch(deque, bicycle_cost, left=0, right=days_length)
    result2 = binarySearch(deque, bicycle_cost2, left=0, right=days_length)
    print(result1, result2)


if __name__ == '__main__':
    main()
