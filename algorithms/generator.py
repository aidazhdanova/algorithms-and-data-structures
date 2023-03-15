def generate_parentheses(n: int, left: int, right: int, current: str) -> None:
    """
    Функция генерирует все возможные  правильные скобочные последовательности(ПСП) длины 2n.
    n: длина ПСП, в данном случае равно 2*n.
    left: количество открывающих скобок, которые еще не закрыты.
    right: количество закрывающих скобок, которые еще не использованы.
    current: строка, текущая ПСП, которая генерируется на данном шаге рекурсии.
    """
    if left == 0 and right == 0:
        print(current)
        return
    # Если остались неиспользованные открывающие скобки, то добавляем открывающую скобку в текущую ПСП и вызываем функцию снова.
    if left > 0:
        generate_parentheses(n, left-1, right, current + '(')
    if right > left:
        generate_parentheses(n, left, right-1, current + ')')

def generate_all_parentheses(n: int) -> None:
    """
    Функция генерирует и печатает все возможные ПСП длины 2n в нужном порядке.
    n: целое число от 0 до 10, длина ПСП.
    """
    generate_parentheses(n*2, n, n, '')

if __name__ == '__main__':
    n = int(input())
    generate_all_parentheses(n)
