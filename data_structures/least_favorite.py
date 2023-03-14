'''В этом коде реализовано удаление элемента односвязного списка по его индексу. 
Функция solution принимает на вход голову списка node и индекс удаляемого элемента index. 
Если нужно удалить первый элемент (голову), то возвращается ссылка на следующий элемент. 
В остальных случаях поиск элемента, который нужно удалить, осуществляется с помощью цикла while. 
Когда элемент найден, он удаляется, а ссылка на голову списка возвращается неизменной. 
Функция test проверяет корректность работы функции solution на примере небольшого списка.'''

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, index):
    # Случай, когда нужно удалить голову
    if index == 0:
        return node.next_item

    # Переменная для обхода списка
    current_node = node
    # Переменная для хранения предыдущего элемента
    previous_node = None
    # Счётчик текущего индекса
    current_index = 0

    # Поиск элемента по индексу
    while current_node and current_index != index:
        previous_node = current_node
        current_node = current_node.next_item
        current_index += 1

    # Если элемент найден, удаляем его
    if current_node:
        previous_node.next_item = current_node.next_item

    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
