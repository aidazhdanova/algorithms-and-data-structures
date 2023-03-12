'''
Данный код содержит класс Stack, реализующий стек, и функцию calculator для выполнения 

арифметических операций в обратной польской записи.

Класс Stack содержит методы push, pop и is_empty, которые позволяют добавлять элементы в стек, 

извлекать элементы из стека и проверять стек на пустоту.

Функция calculator получает на вход список элементов в обратной польской записи и выполняет арифметические операции, используя стек. 

'''

import operator
from typing import List


class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        '''Функция добавления элемента в стек.'''
        self._items.append(item)
    
    def pop(self):
        '''Функция  извлечения элемента из стека.'''
        if not self.is_empty():
            return self._items.pop()
        else:
            raise EmptyStackException("Stack is empty")
    
    def is_empty(self):
        '''Функция проверки стека на пустоту.'''
        return len(self._items) == 0

def calculator(array: List[str]) -> int:
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
    }
    stack = Stack()
    for element in array:
        if element in operators:
            number_2 = stack.pop()
            number_1 = stack.pop()
            result = operators[element](number_1, number_2)
            stack.push(result)
        else:
            stack.push(int(element))
    return stack.pop()

if __name__ == '__main__':
    print(calculator(input().split()))
