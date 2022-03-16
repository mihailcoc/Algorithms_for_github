import sys


def bubble_sort(n, arr):
    was_sorted = True
    for i in range(n - 1):
        changes = 0
        for j in range(0, n - i - 1):
            if int(arr[j]) > int(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changes += 1
                was_sorted = False
        if changes == 0:
            break
        if was_sorted is False:
            print(' '.join(map(str, arr)))

    if was_sorted:
        print(*arr)


def main():
    n = int(input())
    arr = sys.stdin.readline().split()
    bubble_sort(n, arr)


if __name__ == '__main__':
    main()
