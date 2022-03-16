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
        #  print(f' contains lastbox.cat{lastbox.cat}  = self.head.cat {self.head.cat}')
        #  print(f' contains self.head.cat {self.head.cat}')
        #  print(f' contains lastbox.cat {lastbox.cat}')
        #  print(f' contains  cat {cat}')
        while (lastbox):
            print(f' contains while lastbox.cat {lastbox.cat}')
            if cat == lastbox.cat:
                print(f' contains  cat{cat} == lastbox.cat {lastbox.cat}')
                print(f'contains {cat} True {lastbox.data} ')
                return True
            else:
                lastbox = lastbox.nextcat
                # print(f' contains  lastbox.cat {lastbox.cat} = lastbox.nextcat {lastbox.nextcat}')
        print(f'contains {cat} False')
        return False

    def addToEnd(self, newcat, data):
        print(f' addToEnd newcat {newcat}')
        print(f' addToEnd data {data}')
        newbox = Box(newcat, data)
        if self.head is None:
            self.head = newbox
            print(f' addToEnd self.head {self.head.cat} = newbox {newbox.cat}')
            return
        lastbox = self.head
        print(f' addToEnd lastbox.cat {lastbox.cat} = self.head.cat {self.head.cat}')
        while (lastbox.nextcat):
            print(f' addToEnd while (lastbox.nextcat.cat) {lastbox.nextcat.cat}')
            lastbox = lastbox.nextcat
            print(f' addToEnd lastbox {lastbox.cat} = lastbox.nextcat{lastbox.nextcat}')
        lastbox.nextcat = newbox
        print(f' addToEnd lastbox.nextcat.cat {lastbox.nextcat.cat} = newbox.cat{newbox.cat}')
        print(f' addToEnd newbox.cat {newbox.cat}')
        print(f' addToEnd newbox.data {newbox.data}')

    def get(self, cat):
        lastbox = self.head
        #  print(f' contains lastbox.cat{lastbox.cat}  = self.head.cat {self.head.cat}')
        #  print(f' contains self.head.cat {self.head.cat}')
        #  print(f' contains lastbox.cat {lastbox.cat}')
        #  print(f' contains  cat {cat}')
        while (lastbox):
            print(f' contains while lastbox.cat {lastbox.cat}')
            if cat == lastbox.cat:
                print(f' contains  cat{cat} == lastbox.cat {lastbox.cat}')
                print(f'contains {cat} True {lastbox.data} ')
                return lastbox.data
            else:
                lastbox = lastbox.nextcat
                # print(f' contains  lastbox.cat {lastbox.cat} = lastbox.nextcat {lastbox.nextcat}')
        print(f'contains {cat} False')
        return None

    def removeBox(self, rmcat):
        print(f' removeBox rmcat {rmcat}')
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
                print(f'put contains add {int(cmd[1])} {int(cmd[2])}')
            else:
                hash_table.removeBox(int(cmd[1]))
                hash_table.addToEnd(int(cmd[1]), int(cmd[2]))
                print(f'put remove add {int(cmd[1])} {int(cmd[2])}')
        if cmd[0] == 'get':
            if hash_table.contains(int(cmd[1])) is True:
                print(f'get {hash_table.get(int(cmd[1]))}')
            else:
                print(f' get None {int(cmd[1])}')
        if cmd[0] == 'delete':
            if hash_table.contains(int(cmd[1])) is True:
                print(f'delete 1 {hash_table.get(int(cmd[1]))}')
                hash_table.removeBox(int(cmd[1]))
            else:
                print(f' delete None 2 {int(cmd[1])}')
