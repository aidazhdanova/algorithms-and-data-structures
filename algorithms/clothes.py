def sort_clothes(n: int, colors: list) -> list:
    """
    Функция сортирует массив цветов одежды таким образом,
    чтобы сначала шли элементы с цветом 0 (розовый),
    затем элементы с цветом 1 (желтый) и в конце элементы с цветом 2 (малиновый).
    Возвращает отсортированный массив цветов.

    n: количество элементов в массиве
    colors: массив цветов одежды, где 0 — розовый, 1 — желтый, 2 — малиновый
    """
    pink_count, yellow_count, red_count = 0, 0, 0
    # считаем количество элементов каждого цвета
    for color in colors:
        if color == 0:
            pink_count += 1
        elif color == 1:
            yellow_count += 1
        else:
            red_count += 1
    # создаем отсортированный массив
    sorted_clothes = [0] * pink_count + [1] * yellow_count + [2] * red_count
    return sorted_clothes


if __name__ == '__main__':
    n = int(input())
    colors = list(map(int, input().split()))
    print(*sort_clothes(n, colors))
