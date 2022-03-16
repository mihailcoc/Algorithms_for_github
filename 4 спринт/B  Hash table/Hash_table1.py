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


if __name__ == '__main__':
    hash_table = LinkedList()
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'put':
            if hash_table.contains(int(cmd[1])) is False:
                hash_table.addToEnd(int(cmd[1]), int(cmd[2]))
                # print(f'put contains add {int(cmd[1])} {int(cmd[2])}')
            else:
                hash_table.removeBox(int(cmd[1]))
                hash_table.addToEnd(int(cmd[1]), int(cmd[2]))
                # print(f'put remove add {int(cmd[1])} {int(cmd[2])}')
        if cmd[0] == 'get':
            if hash_table.contains(int(cmd[1])) is True:
                print(hash_table.get(int(cmd[1])))
            else:
                print(None)
        if cmd[0] == 'delete':
            if hash_table.contains(int(cmd[1])) is True:
                print(hash_table.get(int(cmd[1])))
                hash_table.removeBox(int(cmd[1]))
            else:
                print(None)