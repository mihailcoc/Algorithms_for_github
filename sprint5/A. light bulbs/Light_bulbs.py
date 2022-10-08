class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


values = []


def solution(root) -> int:

    value = root.value

    left = root.left
    right = root.right
    values.append(value)
    if left:
        solution(left)
    if right:
        solution(right)
    return max(values)


