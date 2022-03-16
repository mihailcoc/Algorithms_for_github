-- ПРИНЦИП РАБОТЫ --
Я реализовал очередь на однос стеке входном.
Все добавляемые в очередь элементы добавляются во входной стек.
Все извлекаемые из очереди элементы извлекаются из входного стека.

Если на момент извлечения из очереди выходной стек пуст,
то выходит ошибка 'pop from empty list'.

Я вдохновился идеей решения из статьи https://ru.stackoverflow.com/questions/1292258/%D0%A1%D1%82%D0%B5%D0%BA-%D0%B4%D0%BE%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0-%D0%BF%D0%BE-%D0%BA%D0%BE%D0%B4%D1%83-%D0%BF%D0%B8%D1%82%D0%BE%D0%BD-%D0%9D%D1%83%D0%B6%D0%BD%D0%B0-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания алгоритма следует, элементы добавляемые в стек будут извлекаться из него, при получении оператора.


Стек -- это порядок LIFO.
Стек инвертирует порядок элементов: первые становятся последними.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление в очередь стоит O(1), потому что добавление во входной стек стоит O(1).

Извлечение из очереди стоит в лучшем случае O(1), когда входной стек не пуст.

В худшем случае извлечение стоит O(n), когда выходной стек пуст,
и тогда требуется переложить все элементы из входного стека в выходной.

Оценим сложность извлечения из очереди в среднем:
Каждый элемент будет переложен из стека в стек ровно один раз.
Это значит, что добавление и извлечение n элементов в сумме будет стоить O(n).
В среднем получаем O(n) / n ~ O(1) -- амортизированная сложность.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Стек, содержащий k элементов, занимает O(k) памяти.
Поэтому и моя очередь будет потреблять O(n1) + O(n2) = O(n) памяти.


import operator


class Stack:
    def __init__(self):
        self.stack_ = []

    def __bool__(self):
        return bool(self.stack_)

    def push(self, item):
        self.stack_.append(item)

    def pop(self):
        try:
            return self.stack_.pop()
        except IndexError:
            raise IndexError('pop from empty list.')

    def size(self):
        return len(self.stack_)


OPERATORS = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.floordiv,
             }


def calculator(maked_string, s=None, operators=OPERATORS, c=int):
    s = Stack()
    for el in maked_string:
        if el not in operators:
            try:
                s.push(c(el))
            except ValueError:
                raise TypeError(f' "{c}" - wrong type.')
        else:
            first = s.pop()
            sec = s.pop()
            try:
                s.push(int(operators[el](int(sec), int(first))))
            except ZeroDivisionError:
                raise ZeroDivisionError(f'Деление на 0 "{sec} {el} {first}".')
            except TypeError:
                raise TypeError(
                    f'Неподдерживаемая операция "{el}" для {el.__name__}.')
    return s.pop()


def main():

    string = input().split()
    result = calculator(string)
    print(result)


if __name__ == '__main__':
    main()
