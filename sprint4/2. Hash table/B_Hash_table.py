#  https://contest.yandex.ru/contest/24414/run-report/64775511/

-- ПРИНЦИП РАБОТЫ --
Я реализовал решение по принципу связного списка.
Первая часть решения заключается в формировании массива из 100 000 элементов. 
Код выбирает последние 5 символов из 9 - ти значного числа ID сотрудника
и применяет их как номер строки в массиве.
Затем вторая часть алгоритма помещает данные об ID сотрудника и его заработной плате а связный список
а связный список помещается в ячейку значения в массиве , где ключом является последние 5 символов ID.

Я вдохновился идеей решения из статьи: Связный список на Python: Коты в коробках.
https://habr.com/ru/company/otus/blog/470828/

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания следует что, при возникновении коллизии в 5 - ти значных номерах строк массива, 
элементы будут помещены в связный список, закреплённый за строкой массива.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Распределение с помощью связных списков демонстрирует среднее время работы O(n).
Метод добавления элемента демонстрирует среднее время работы O(n) потому что при добавлении
элемент добавляется в конец списка а для этого необходимо перебрать все элементы поочерёдно.
Метод удаления элемента демонстрирует среднее время работы O(3n) потому что при удалении
элемент находится а для этого необходимо перебрать все элементы поочерёдно.
А затем элементы снова просматриваются поочерёдно чтобы найти значение ключа и вывести его на
печать. И ещё раз все элменты просматриваются поочерёдно для находжения элмента при удалении.
Метод нахождения элемента демонстрирует среднее время работы O(n) потому что при нахождении
элемента необходимо перебрать все элементы поочерёдно.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Величина массива соответствует величине элементов в тесте и не превышает 100 000 элементов.


class Box:
    def __init__(self, cat, data):
        self.nextcat = None
        self.cat = cat
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, cat: int) -> bool:
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newcat: int, data: int):
        newbox = Box(newcat, data)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    def get(self, cat: int) -> int:
        lastbox = self.head

        while (lastbox):
            if cat == lastbox.cat:
                return lastbox.data
            else:
                lastbox = lastbox.nextcat
        return None

    def removeBox(self, rmcat: int):
        headcat = self.head

        if headcat is not None:
            if headcat.cat == rmcat:
                self.head = headcat.nextcat
                value = headcat.data
                headcat = None
                return value
        while headcat is not None:
            if headcat.cat == rmcat:
                break
            lastcat = headcat
            headcat = headcat.nextcat
        if headcat is None:
            return
        lastcat.nextcat = headcat.nextcat
        headcat = None


class Hashtable:
    def __init__(self):
        self.array = [] * 100000

    def put(self, hk: int, value: list):
        self.array[hk] = hk, value

    def getcell(self, hk: int):
        hk, value = self.array[hk]
        return value


def run_array():
    hash_table = Hashtable()
    value = list()
    for i in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'put':
            value = hash_table.getcell(int(cmd[1][-5:]))
            if value.contains(int(cmd[1])) is False:
                value.addToEnd(int(cmd[1]), int(cmd[2]))
                hash_table.put(int(cmd[1][-5:]), value)
            else:
                value.removeBox(int(cmd[1]))
                value.addToEnd(int(cmd[1]), int(cmd[2]))
                hash_table.put(int(cmd[1][-5:]), value)
        if cmd[0] == 'get':
            value = hash_table.getcell(int(cmd[1][-5:]))
            print(value.get(int(cmd[1])))
        if cmd[0] == 'delete':
            value = hash_table.getcell(int(cmd[1][-5:]))
            if value.contains(int(cmd[1])) is True:
                print(value.get(int(cmd[1])))
                value.removeBox(int(cmd[1]))
                hash_table.put(int(cmd[1][-5:]), value)
            else:
                print(None)


if __name__ == '__main__':
    run_array()
