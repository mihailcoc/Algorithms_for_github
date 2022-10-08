class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:

    if node is None:
        print('The list has no element to reverse')
        return
    previous_node = node   # последний узел
    current_node = previous_node.next   # текущая node следует за последней (головой)
    previous_node.next = None   # предыдущая ссылка последнего узла (головы) д.б. None
    previous_node.prev = current_node   # следующая ссылка (головы) равна текущей
    while current_node is not None:
        current_node.prev = current_node.next   # предыдущие ссылки узлов в исходном списке заменяются на следующие
        current_node.next = previous_node   # следующие ссылки узлов в исходном списке заменяются на предыдущие
        previous_node = current_node   # значения предыдущих узлов заменяются на следующие
        current_node = current_node.prev   # значения следующих узлов заменяются на предыдущие
    head = previous_node   # новая голова списка равна первому элементу
    return head