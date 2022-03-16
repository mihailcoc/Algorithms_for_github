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
    print(f'check_correct_bst key = root.value {root.value}')
    print(f'check_correct_bst keys {keys}')
    print(f'check_correct_bst removed{removed}')
    if root == None:
        return 0
    key = root.value
    if key == removed:
        raise Exception('Found deleted key in the result BST')
    if key not in keys:
        print(f'if key{key}  not in keys {keys}')
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


def find_min(root: Node) -> Node:
    print(f'find_min root.value {root.value}')
    if root.left is not None:
        print(f'find_min if root.left is not None {root.left.value}')
        return find_min(root.left)
    else:
        print(f'find_min root.value {root.value}')
        return root


def remove(root: Node, key: int) -> Node:
    if root is None:
        return None
    print(f'key {key}  root.value {root.value}')
    if key < root.value:
        print(f'remove if str(key){key} < str(root.value) {root.value}')
        remove(root.left, key)
        return root
    elif key > root.value:
        print(f'remove elif str(key){key} > str(root.value) {root.value}')
        remove(root.right, key)
        return root
    if key == root.value:
        print(f'elif key {key} = root.value {root.value}')
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            print(f'if root.left is not None {root.left.value} and root.right is not None {root.right.value} ')
            min_key = find_min(root.right).value
            print(f'remove  min_key.value {min_key}')
            root.key = min_key
            root.right = remove(root.right, min_key)
            print('break')
        return root


if __name__ == '__main__':
    test_type = input()
    n = int(input())
    tree, keys = read_tree(n)
    if test_type == 'correctness':
        to_remove = int(input())
        print(tree)
        print(to_remove)
        tree = remove(tree, to_remove)
        expected_size = n
        if to_remove in keys:
            print(f'if to_remove {to_remove} in keys {keys}')
            expected_size -= 1
            print(f'expected_size -= 1 {expected_size}')
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