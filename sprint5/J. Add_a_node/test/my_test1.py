import sys
sys.setrecursionlimit(2000000)


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def read_tree(n):
    keys = set()
    if n == 0:
        return None, keys
    nodes = [Node() for i in range(n)]
    for i in range(n):
        idx, key, lf, rg = map(int, input().split())
        keys.add(key)
        nodes[idx - 1].value = key
        if lf != -1:
            nodes[idx - 1].left = nodes[lf - 1]
        if rg != -1:
            nodes[idx - 1].right = nodes[rg - 1]
    return nodes[0], keys


def check_correct_bst(root, keys, removed):
    if root == None:
        return 0
    key = root.value
    if key == removed:
        raise Exception('Found deleted key in the result BST')
    if key not in keys:
        raise Exception('Unknown key')
    sz = 0
    if root.left != None:
        if root.left.value > key:
            raise Exception('Left child is bigger than its parent')
        sz += check_correct_bst(root.left, keys, removed)
    if root.right != None:
        if root.right.value < key:
            raise Exception('Right child is smaller than its parent')
        sz += check_correct_bst(root.right, keys, removed)
    return sz + 1


def insert(root: Node, key: int) -> Node:
    print(f' insert_recursively root.value {root.value}')
    print(f' insert_recursively root.left {root.left}')
    print(f' insert_recursively root.right {root.right}')
    print(f' insert_recursively key {key}')
    if key < root.value:
        print(f'if str(key){key} < str(root.value) {root.value}')
        if root.left == None:
            root.left = Node(left=None, right=None, value=key)
        else:
            insert(root.left, key)
    elif key >= root.value:
        print(f'elif str(key){key} >= str(root.value) {root.value}')
        if root.right == None:
            root.right = Node(left=None, right=None, value=key)
        else:
            insert(root.right, key)
    return root


def print_tree(tree):
    if tree == None:
        return
    print(f'print_tree tree.value {tree.value}')
    print(tree.value)
    print("Go left")
    print(f'print_tree Go left tree.value {tree.value}')
    print(f'print_tree Go left tree.left {tree.left}')
    print_tree(tree.left)
    print("Go right")
    print(f'print_tree Go right tree.value {tree.value}')
    print(f'print_tree Go left tree.right {tree.right}')
    print_tree(tree.right)


if __name__ == '__main__':
    n = int(input())
    tree, keys = read_tree(n)
    print(f'tree.value {tree.value}')
    print(f'tree.left {tree.left}')
    print(f'tree.right {tree.right}')
    print(f'keys {keys}')
    to_insert = int(input())
    print(f'to_insert {to_insert}')
    tree = insert(tree, to_insert)
    print("print_tree(tree)")
    print(f'tree.value2 {tree.value}')
    print(f'root.left2 {tree.left}')
    print(f'root.right2 {tree.right}')
    print_tree(tree)