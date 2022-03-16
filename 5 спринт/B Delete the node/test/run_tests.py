from solution import remove

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


if __name__ == '__main__':
    test_type = input()
    n = int(input())
    tree, keys = read_tree(n)
    if test_type == 'correctness':
        to_remove = int(input())
        tree = remove(tree, to_remove)
        expected_size = n
        if to_remove in keys:
            expected_size -= 1
        try:
            if check_correct_bst(tree, keys, to_remove) != expected_size:
                raise Exception('Size of Bst does not match with the answer')
            print('Correct')
        except Exception as err:
            print(err.args[0])
    else:
        for key in keys:
            tree = remove(tree, key)
        if tree != None:
            print('FAIL: non-null')
        else:
            print('OK: null')