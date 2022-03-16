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
        self.array = []

    def make_table(self, N: int):
        for i in range(N):
            self.array.append((i, LinkedList()))
        return self.array

    def put(self, hk: int, value: list):
        self.array[hk] = hk, value

    def getcell(self, hk: int):
        hk, value = self.array[hk]
        return value


def run_array():
    hash_table = Hashtable()
    hash_table.make_table(100000)
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
