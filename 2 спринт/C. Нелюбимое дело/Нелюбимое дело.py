def get_node_by_index(node, index):

    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, index):

    if index == 0:
        node = node.next_item
        return node
    previous_node = get_node_by_index(node, index - 1)
    following_node = get_node_by_index(node, index + 1)
    previous_node.next_item = following_node
    return node