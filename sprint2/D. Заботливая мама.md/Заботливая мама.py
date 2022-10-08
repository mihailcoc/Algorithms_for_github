def solution(node, idx) -> int:
    
    index = 0
    caring_mother_list = []
    while node:
        caring_mother_list.append(node.value)
        if node.value == idx:
            return index
        node = node.next_item
        index += 1
    return -1