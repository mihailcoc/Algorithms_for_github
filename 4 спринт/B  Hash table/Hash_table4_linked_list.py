class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, catIndex):
        lastbox = self.head
        # boxIndex = 0
        boxIndex = self.head.cat
        while boxIndex <= catIndex:
            while (lastbox):
                if boxIndex == catIndex:
                    if lastbox is not None:
                        return lastbox.cat
                    else:
                        return lastbox
                boxIndex = boxIndex + 1
                lastbox = lastbox.nextcat
            return lastbox

    def contains(self, cat):
        lastbox = self.head
        print(f' contains lastbox{lastbox}  = self.head {self.head}')
        while (lastbox):
            print(f' while lastbox.cat {lastbox.cat}')
            if cat == lastbox.cat:
                print(f' contains  cat{cat} == lastbox.cat {lastbox.cat}')
                print('contains True')
                return True
            else:
                lastbox = lastbox.nextcat
                # print(f' contains  lastbox.cat {lastbox.cat} = lastbox.nextcat.cat {lastbox.nextcat.cat}')
        print('contains False')
        return False

    def addToEnd(self, newcat):
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    def removeBox(self, rmcat):
        headcat = self.head

        if headcat is not None:
            if headcat.cat == rmcat:
                self.head = headcat.nextcat
                headcat = None
                return
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
            if cmd[0]:
                hash_table.addToEnd(int(cmd[1]))
                print(f'put {int(cmd[1])}')
            else:
                print('put None')
                #  print(hash_table)
        if cmd[0] == 'get':
            if hash_table.contains(int(cmd[1])) is True:
                print('hash_table.contains(int(cmd[1])) is True')
                hash_table.get(int(cmd[1]))
            else:
                print(f' get None {int(cmd[1])}')
        if cmd[0] == 'delete':
            if hash_table:
                hash_table.removeBox(int(cmd[1]))
            else:
                print(f' delete None {int(cmd[1])}')
