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


def remove(root, key):
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

    
