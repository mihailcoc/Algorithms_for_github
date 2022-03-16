import sys


def quicksort(array, left, right):
    def inner_quicksort(array, left, right):
        if left >= right - 1:
            return array
        start_point = left
        end_point = right
        pivot_index = (left + right) // 2
        pivot = array[pivot_index]
        while left < right:
            if left != right:
                array[left], array[right] = array[right], array[left]
            while left < right and array[left] < pivot:
                left += 1
            while left < right and array[right] > pivot:
                right -= 1
        inner_quicksort(array, start_point, left)
        inner_quicksort(array, left + 1, end_point)
    inner_quicksort(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    def people(name, task, score):
        return -int(task), int(score), name
    n = int(input())
    array = [people(*input().split()) for _ in range(n)]
    result = (login for _, _, login in quicksort(array, 0, n - 1))
    print(*result, sep="\n")
