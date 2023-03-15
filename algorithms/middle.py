def find_median(n: int, m: int, north: list, south: list) -> float:
    """
    Функция для нахождения медианы среди всех значений численности населения.
    - n: количество островов в северной части архипелага
    - m: количество островов в южной части архипелага
    - north: отсортированный список численности населения в северной части архипелага
    - south: отсортированный список численности населения в южной части архипелага
    """
    # Объединяем отсортированные списки в один список
    merged = north + south
    merged.sort()
    # Находим медиану в объединенном списке
    total = n + m
    mid = total // 2
    if total % 2 == 0:
        # Если количество элементов четное, то находим среднее двух соседних элементов
        return (merged[mid-1] + merged[mid]) / 2.0
    else:
        # Если количество элементов нечетное, то находим средний элемент
        return merged[mid]


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    north = list(map(int, input().split()))
    south = list(map(int, input().split()))
    result = find_median(n, m, north, south)
    print(result)
