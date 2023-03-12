from collections import Counter

def max_points(array: str, count: int) -> int:
    '''Функция max_points вычисляет максимальное количество очков, которое можно набрать в игре.
    array - это строка длиной в 16 символов, состоящая из цифр от 0 до 9 и точек. 
    Точки представляют пустые ячейки на игровом поле. 
    count - это максимальное количество раз, которое цифра может появиться на игровом поле.
    Возвращаемое значение функции - это максимальное количество очков, которое можно набрать в игре.'''
    count *= 2
    nums_dict = Counter(array.replace('.', ''))
    return sum(1 for value in nums_dict.values() if value <= count)

if __name__ == '__main__':
    count = int(input())
    array = ''.join([input().strip() for _ in range(4)])
    print(max_points(array, count))
