from functools import cmp_to_key

def compare(x, y):
    """Функция сравнения для сортировки чисел."""
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return -1
    else:
        return 1

def find_max_number(n: int, numbers: list) -> int:
    """
    Функция для нахождения самого большого числа, которое можно составить из заданных чисел.
    n: количество чисел,
    numbers: список чисел.
    """
    # Сортируем числа по убыванию с помощью собственной функции сравнения
    numbers = sorted(numbers, key=cmp_to_key(compare))
    # Соединяем числа в одно число
    max_number = int(''.join(str(number) for number in numbers))
    return max_number


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    max_number = find_max_number(n, numbers)
    print(max_number)
