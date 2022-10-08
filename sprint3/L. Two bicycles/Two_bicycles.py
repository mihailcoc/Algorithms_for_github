import sys


def binarySearch(arr, x, left, right):
    if right <= left:  # промежуток пуст
        return -1
    mid = int((left + right) // 2)
    middle = int(arr[mid])
    middle_minus_1 = int(arr[mid - 1])
    # print(f'левая половина"{left}".')
    # print(f'правая половина"{right}".')
    # print(f'индекс середины "{mid}"')
    # print(f'значение середины "{middle}"')
    mid1 = mid - 1
    # print(f'индекс минус один "{mid1}"')
    # print(f'значение середина минус один"{middle_minus_1}"')
    if mid1 < 0:
        if middle >= x:
            return mid + 1
        elif x <= middle:
            return binarySearch(arr, x, left, mid)
        else:
            return binarySearch(arr, x, mid + 1, right)
    else:
        if (middle >= x) and (middle_minus_1 < x):
            return mid + 1
        elif x <= middle:
            return binarySearch(arr, x, left, mid)
        else:
            return binarySearch(arr, x, mid + 1, right)


def main():
    arr = []
    limit = int(input())
    n = sys.stdin.readline().split()
    x = int(input())
    index = binarySearch(n, x, left=0, right=limit)
    index2 = binarySearch(n, x * 2, left=0, right=limit)
    print(index, index2)


if __name__ == '__main__':
    main()

