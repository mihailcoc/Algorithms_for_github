import sys


def bubble_sort(n, arr):
    numbers_moved = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                numbers_moved == True
        if numbers_moved == True:
            print(' '.join(map(str, arr)))
        else:
            break


def main():
    n = int(input())
    arr = sys.stdin.readline().split()
    bubble_sort(n, arr)


if __name__ == '__main__':
    main()


def bubble_sort(items):
    was_sorted = True
    for ...
        changes = 0
        for ...
            if ...
                changes += 1
                was_sorted = False

        if changes == 0:
            break

        print(*items)

    if was_sorted:
        print(*items)