import sys


def item_to_insert(lhs: str, rhs: str):
    if int(lhs + rhs) > int(rhs + lhs):
        return True
    return False


def insertion_sort_by_comparator(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return [str(a) for a in array]


if __name__ == '__main__':
    _ = input()
    arr = sys.stdin.readline().split()
    numbers = insertion_sort_by_comparator(arr, item_to_insert)
    print(*numbers, sep='')

