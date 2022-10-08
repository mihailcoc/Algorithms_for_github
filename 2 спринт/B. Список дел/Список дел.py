def solution(node) -> None:

    while node:
        print(node.value, end='\n')
        node = node.next_item