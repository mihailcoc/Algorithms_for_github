from node import Node


def insert(root: Node, key: int) -> Node:
    if key < root.value:
        if root.left == None:
            root.left = Node(left=None, right=None, value=key)
        else:
            insert(root.left, key)
    elif key >= root.value:
        if root.right == None:
            root.right = Node(left=None, right=None, value=key)
        else:
            insert(root.right, key)
    return root
