class Hashtable:
    def __init__(self):
        self.stack_ = [] * 100000

    def __bool__(self):
        return bool(self.stack_)

    def make_table(self):
        for i in range(100000):
            self.stack_.append((i, 0))
        return self.stack_

    def put(self, hk, value):
        self.stack_[hk] = hk, value

    def delete(self, hk):
        hk, value = self.stack_[hk]
        if value == 0:
            print('None')
        else:
            print(value)
            self.stack_[hk] = hk, 0

    def get(self, hk: int):
        hk, value = self.stack_[hk]
        if value == 0:
            print('None')
        else:
            print(value)


if __name__ == '__main__':
    hash_table = Hashtable()
    hash_table.make_table()
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'put':
            if cmd[0]:
                hash_table.put(int(cmd[1]), int(cmd[2]))
            else:
                print('None')
        if cmd[0] == 'get':
            if hash_table:
                hash_table.get(int(cmd[1]))
            else:
                print('None')
        if cmd[0] == 'delete':
            if hash_table:
                hash_table.delete(int(cmd[1]))
            else:
                print('None')
