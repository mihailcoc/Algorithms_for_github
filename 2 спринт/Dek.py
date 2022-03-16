-- ПРИНЦИП РАБОТЫ --
Я реализовал очередь на циклическом буфере.
Все добавляемые в очередь элементы добавляются в циклический буфер.
Все извлекаемые из очереди элементы извлекаются из циклического буфера.

Если на момент извлечения из очереди выходной буфер пуст,
то выходит ошибка 'error'. Извлечь элемент можно, как из головы буфера, так и из конца.

Я вдохновился идеей решения из статьи https://pythobyte.com/double-ended-queue-8e3d9271/
-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания алгоритма следует, что чем раньше элемент добавился в очередь,
тем раньше он будет из неё извлечён.

Выходной буфер хранит элементы в порядке, обратном тому,
в каком они пришли во входной.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление в очередь стоит O(1), потому что добавление во входной стек стоит O(1).

Извлечение из очереди стоит в лучшем случае O(1), когда выходной стек не пуст.

В худшем случае извлечение стоит O(n), когда выходной стек пуст,
и тогда требуется переложить все элементы из входного стека в выходной.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Если очередь содержит n элементов, то входной стек содержит n1 элементов,
и выходной стек содержит n2 элементов, причём n1 + n2 = n

Стек, содержащий k элементов, занимает O(k) памяти.
Поэтому и моя очередь будет потреблять O(n1) + O(n2) = O(n) памяти.

class Deque:
    def __init__(self, limit):
        self.queue = [None] * limit
        self.max_n = limit
        self.head = 0
        self.tail = 1
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def is_full(self):
        return self.queue_size == self.max_n

    def index_position(self, index, value):
        if value == 1:
            return (index + value) % self.max_n
        else:
            return (index - 1 + self.max_n) % self.max_n

    def push_back(self, item):
        if not self.is_full():
            self.tail = self.index_position(index=self.tail, value=-1)
            self.queue[self.tail] = item
            self.queue_size += 1
        else:
            raise IndexError('error')

    def push_front(self, item):
        if not self.is_full():
            self.head = self.index_position(index=self.head, value=1)
            self.queue[self.head] = item
            self.queue_size += 1
        else:
            raise IndexError('error')

    def pop_front(self):
        if not self.is_empty():
            item = self.queue[self.head]
            self.head = self.index_position(index=self.head, value=-1)
            self.queue_size -= 1
            return item
        else:
            raise IndexError('error')

    def pop_back(self):
        if not self.is_empty():
            item = self.queue[self.tail]
            self.tail = self.index_position(index=self.tail, value=1)
            self.queue_size -= 1
            return item
        else:
            raise IndexError('error')


def curcular_queue():
    commands_number = int(input())
    limit = int(input())
    deque = Deque(limit)
    for _ in range(commands_number):
        command, *parameters = input().split()
        try:
            value = getattr(deque, command)(*parameters)
            if value is not None:
                print(value)
        except (OverflowError, IndexError):
            print('error')
        except AttributeError:
            raise AttributeError(f'Команда - {command} не найдена')


if __name__ == '__main__':
    curcular_queue()
