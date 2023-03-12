from typing import List, Optional

class DequeFullError(Exception):
    pass


class EmptyDequeError(Exception):
    pass


class Deque:
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._items = [None] * max_size
        self._head = 0  # Индекс головы
        self._tail = 0  # Индекс хвоста
        self._size = 0  # Текущий размер дека

    def push_back(self, value: int) -> None:
        '''Функция добавления элемента в конец дека.'''
        if self._size == self._max_size:
            raise DequeFullError("error")
        self._items[self._tail] = value
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1

    def push_front(self, value: int) -> None:
        '''Функция добавления элемента в начало дека'''
        if self._size == self._max_size:
            raise DequeFullError("error")
        self._head = (self._head - 1) % self._max_size
        self._items[self._head] = value
        self._size += 1

    def pop_front(self) -> Optional[int]:
        '''Функция удаления первого элемента дека.'''
        if self._size == 0:
            raise EmptyDequeError("error")
        value = self._items[self._head]
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return value

    def pop_back(self) -> Optional[int]:
        '''Функция удаления последнего элемента дека.'''
        if self._size == 0:
            raise EmptyDequeError("error")
        self._tail = (self._tail - 1) % self._max_size
        value = self._items[self._tail]
        self._size -= 1
        return value


if __name__ == '__main__':
    count: int = int(input())
    max_size: int = int(input())

    deque: Deque = Deque(max_size)

    for _ in range(count):
        command: List[str] = input().split()
        operation = getattr(deque, command[0])
        if len(command) > 1:
            try:
                operation(int(command[1]))
            except DequeFullError as error:
                print(str(error))
        else:
            try:
                result = operation()
                if result is not None:
                    print(result)
            except EmptyDequeError as error:
                print(str(error))
