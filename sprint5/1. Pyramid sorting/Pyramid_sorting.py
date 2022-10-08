-- ПРИНЦИП РАБОТЫ --
Сначала алгоритм принимает базу из участников. Логин, количество задач
и количество штрафов. Затем Алгоритм с помощью встроенного метода
__gt__ сравнивает поочерёдно каждый элемент и по результатам
сравнения запускает алгоритм sift_up.
Далее Запускается второй алгоритм, где поочерёдно берутся элементы
и перекладываются из одного массива в другой. Также происходит
сравнение каждого элемента итеративно и при необходимости элементы
передвигаются при помощи алгоритма sift_down.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Встроенный метод __gt__ помогает избежать большое количество
сравнений if elif else..

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность составления словаря O(N), потому что составление массива
происходит путём прохода поочерёдно всех элементов массива из условия.
Далее при сравнении элементов используется бинарная куча, сложность O(LogN)


class Participant:
    def __init__(self, login: str, task: int, penalty: int):
        self.login = login
        self.task = task
        self.penalty = penalty
 
    def __gt__(self, second):
        key_first = [-self.task, self.penalty, self.login]
        key_second = [-second.task, second.penalty, second.login]
        return key_first > key_second
 
 
class Pyramid_Sorting:
    def __init__(self, N: int):
        self.heap = [Participant("1", 1, 1) for _ in range(N + 1)]
        self.size = 0
 
    def sift_up(self, index: int):
        if index == 1:
            return
        while index != 1:
            parent_index = index // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
        return
 
    def sift_down(self, index: int):

        while self.size >= 2 * index:
            left = 2 * index
            right = 2 * index + 1
            if right <= self.size and self.heap[left] > self.heap[right]:
                index_largest = right
            else:
                index_largest = left
            if self.heap[index] > self.heap[index_largest]:
                self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
                index = index_largest
            else:
                return

    def heap_add(self, key):
        self.size += 1
        self.heap[self.size] = key
        self.sift_up(self.size)
 
    def heap_get_max_priority(self):
        max_elem = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.sift_down(1)
        return max_elem
 
    def heapsort(self) -> set:
        sorted_array = []
        while self.size > 0:
            result = self.heap_get_max_priority()
            sorted_array.append(result.login)
        return sorted_array


def main():
    N = int(input())
    heap = Pyramid_Sorting(N)
    for i in range(0, N, 1):
        login, task, penalty = input().split()
        heap.heap_add(Participant(login, int(task), int(penalty)))
    print('\n'.join(map(str, heap.heapsort())))

 
if __name__ == '__main__':
    main()
