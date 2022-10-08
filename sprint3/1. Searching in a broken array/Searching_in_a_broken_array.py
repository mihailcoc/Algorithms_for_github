# 56369428
# https://contest.yandex.ru/contest/23815/run-report/56369428/

-- ПРИНЦИП РАБОТЫ --.
Код выбирает опорную точку, которая определяет левую и правую части сортируемых данных.
Опорной точкой является элемент находящийся в середине массива и индекс получается в результате 
целочисленного деления сумм индексов начального и конечного элементов.

Когда код больше не может искать элемент, цикл завершается, и искомый индекс возвращается вызывающей функции.
Поиск элемента происходит итеративно.

Я вдохновился идеей решения из статьи https://stackabuse.com/quicksort-in-python/

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания следует, что на первой итерации средний элемент будет выбран для сравнения.
Далее мы проходимся по всем элементам рекурсивно и сравниваем их с искомым элементом.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Скорость работы бинарного поиска имеет логарифмическую зависимость от размера входных данных

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Требуется реализовать функцию, осуществляющую поиск в сломанном массиве.
Массив содержит n элементов. Значит пространственная сложность О(n).


def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    else:
        return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6