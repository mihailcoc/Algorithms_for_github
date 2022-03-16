# https://contest.yandex.ru/contest/23815/run-report/56691926/
 
-- ПРИНЦИП РАБОТЫ --
Я реализовал решение по принципу быстрой сортировки - quicksort.
Первая часть сортировки заключается в разбиении данных. 
Код выбирает опорную точку, которая определяет левую и правую части сортируемых данных.
Внутренний цикл в этом примере последовательно ищет элементы, находящиеся в неправильном месте, и меняет их местами.
Когда код больше не может поменять элементы, цикл завершается, и новая опорная точка возвращается вызывающей функции.
Я вдохновился идеей решения из статьи https://pythonist.ru/bystraya-sortirovka-na-python/

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания следует, что на первой итерации самый левый элемент будет выбран средним.
Далее мы проходимся по всем элементам слева направо.
 
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Быстрая сортировка редко демонстрирует наихудшее время работы. 
Однако даже модифицированный версии быстрой сортировки могут давать наихудшее время работ О(n2).
В среднем время работы Quicksort составляет O(n*logn).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Быстрая сортировка со случайными центрами имеет пространственную сложность
Средний случай = O(logN) 
Худший случай = O(N)
Худший случай возникает, когда опорным элементом выбирается либо крайний левый либо крайний правый элемент.
 

def quick_sort(data: str, start: int, end: int):
    def partition(start: int, end: int):
        if start >= end:
            return
        pivot = start
        for item in range(start, end):
            if data[end] > data[item]:
                data[pivot], data[item] = data[item], data[pivot]
                pivot += 1
        data[pivot], data[end] = data[end], data[pivot]
        partition(start, pivot - 1)
        partition(pivot + 1, end)
    partition(0, len(data) - 1)
    return data


if __name__ == '__main__':
    def people(name, task: int, score: int):
        return -int(task), int(score), name
    n = int(input())
    array = [people(*input().split()) for _ in range(n)]
    result = (login for _, _, login in quick_sort(array, 0, n - 1))
    print(*result, sep="\n")
