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


def search_iteratively(root, x):
    while root is not None:
        if root.value == x:
            return root
        elif x < root.value:
            root = root.left
        else:  # x > root.key:
            root = root.right
    return None


def replace_child(root, parent, old, new):
    if parent is None:
        root = new
    elif parent.left == old:
        parent.left = new
    elif parent.right == old:
        parent.right = new
    return root


def remove(root: Node, key: int) -> Node:
    res = search_iteratively(root, key)
    if res is None:
        return root
    else:
        parent = None
        v = root

        while True:
            if v is None:
                return
            if key < v.value:
                parent = v
                v = v.left
            elif key > v.value:
                parent = v
                v = v.right
            else:  # key == v.value
                break

        result = None

        if v.left is None:
            result = v.right
        elif v.right is None:
            result = v.left
        else:
            min_node_parent = v
            min_node = v.right
            while min_node.left is not None:
                min_node_parent = min_node
                min_node = min_node.left

            result = v
            v.value = min_node.value
            root = replace_child(root, min_node_parent, min_node, min_node.right)

        root = replace_child(root, parent, v, result)
        return root


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