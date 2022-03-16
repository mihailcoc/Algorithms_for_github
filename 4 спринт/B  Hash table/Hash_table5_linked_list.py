class Node:
    def __init__(self, hk, data):
        self.next = None
        self.hk = hk
        self.data = data

    def append(self, hk, data):
        end = Node(hk, data)
        n = self
        while (n.next):
            n = n.next
        n.next = end


if __name__ == '__main__':
    #  print(hash_table)
    for _ in range(int(input())):
        cmd = input().split()
        hash_table = Node(cmd[1], cmd[2])
        if cmd[0] == 'put':
            if cmd[0]:
                hash_table.append(int(cmd[1]), int(cmd[2]))
                print(hash_table)
            else:
                print('None')
                #  print(hash_table)
        if cmd[0] == 'get':
            if hash_table:
                hash_table.get(int(cmd[1]))
            else:
                print('None')
        if cmd[0] == 'delete':
            if hash_table:
                hash_table.removeBox(int(cmd[1]))
            else:
                print('delete None')
