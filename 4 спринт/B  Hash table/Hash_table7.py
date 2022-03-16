class Box:
    def __init__(self, cat, data):
        self.nextcat = None
        self.cat = cat
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, cat):
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newcat, data):
        newbox = Box(newcat, data)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    def get(self, cat):
        lastbox = self.head

        while (lastbox):
            if cat == lastbox.cat:
                return lastbox.data
            else:
                lastbox = lastbox.nextcat
        return None

    def removeBox(self, rmcat):
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
        self.stack_ = []

    def make_table(self, N, linked_list: list):
        for i in range(0, N, 1):
            self.stack_.append((i, LinkedList()))
        return self.stack_

    def put(self, hk: int, value: list):
        print(f'put Hashtable hk {hk}')
        self.stack_[hk] = hk, value
        print(f'put Hashtable end {hk}')

    def getcell(self, hk: int):
        print(f'getcell hk {hk}')
        hk, value = self.stack_[hk]
        print(f'getcell return value end {hk}')
        return value


if __name__ == '__main__':
    hash_table = Hashtable()
    hash_table.make_table(148000, LinkedList())
    for i in range(int(input())):
        cmd = input().split()
        print(f'i {i}')
        cell_numder = int()
        cell_numder = int(cmd[1][-6:])
        if cell_numder >= 148000:
            cell_numder = int(cmd[1][-5:])
        print(f'main {(cmd[0])} {int(cmd[1])} cell_numder len = 9 {cell_numder}')
        if cmd[0] == 'put':
            print(f'main put {cmd[0]} cmd[1] {cmd[1]} cell_numder {cell_numder} ')
            value = hash_table.getcell(cell_numder)
            print(f'put hash_table_list {value}')
            if value.contains(int(cmd[1])) is False:
                value.addToEnd(int(cmd[1]), int(cmd[2]))
                print(f'put new value {value}')
                hash_table.put(cell_numder, value)
                print('put end')
            else:
                value.removeBox(int(cmd[1]))
                value.addToEnd(int(cmd[1]), int(cmd[2]))
                hash_table.put(cell_numder, value)
                print('put end')
        if cmd[0] == 'get':
            print(f'main get {cmd[0]}  cell_numder {cell_numder} ')
            value = hash_table.getcell(cell_numder)
            #  print(f'get value {value}')
            #  value = hash_table_list
            #  print(f'get hash_table_list {LinkedList}')
            if value.contains(int(cmd[1])) is True:
                print(value.get(int(cmd[1])))
                print('get end')
            else:
                print(f' get None {int(cmd[1])}')
                print('get end')
        if cmd[0] == 'delete':
            print(f'main delete {cmd[0]}  cell_numder {cell_numder} ')
            value = hash_table.getcell(cell_numder)
            #  print(f'delete value {value}')
            #  value = hash_table_list
            #  print(f'delete hash_table_list {LinkedList}')
            if value.contains(int(cmd[1])) is True:
                print(value.get(int(cmd[1])))
                value.removeBox(int(cmd[1]))
                hash_table.put(cell_numder, value)
                print('delete end')
            else:
                print(f' delete None  {int(cmd[1])}')
                print('delete end')