def satisfied_children() -> int:
    """
    Функция запрашивает у пользователя количество детей, факторы жадности каждого ребенка, 
    количество печенек и размеры печенек. Функция возвращает количество детей, 
    которые останутся довольными, то есть количество детей, которым можно дать печенье 
    такого размера, чтобы их фактор жадности был не меньше размера печенья.
    """
    num_children = int(input())
    greed_factors = list(map(int, input().split()))
    num_cookies = int(input())
    cookie_sizes = list(map(int, input().split()))
    # сортируем списки факторов жадности и размеров печенек по возрастанию
    greed_factors.sort()
    cookie_sizes.sort()
    i = j = count = 0
    # проходим по списку факторов жадности и пытаемся удовлетворить каждого ребенка
    while i < num_children and j < num_cookies:
        if greed_factors[i] <= cookie_sizes[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    return count

print(satisfied_children())
