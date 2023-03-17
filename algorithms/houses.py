from typing import List


def max_num_of_houses(n: int, k: int, prices: List[int]) -> int:
    """
    Функция принимает на вход количество домов, бюджет и список стоимостей домов.
    Возвращает наибольшее количество домов, которое можно купить за данный бюджет.
    n: количество домов
    k: бюджет
    prices: список стоимостей домов
    """
    # Сортируем стоимости домов по возрастанию
    prices.sort()

    # Идём по списку стоимостей и покупаем дома, пока не кончится бюджет
    houses = 0
    for price in prices:
        if price <= k:
            k -= price
            houses += 1
        else:
            break

    return houses


if __name__ == '__main__':
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    print(max_num_of_houses(n, k, prices))