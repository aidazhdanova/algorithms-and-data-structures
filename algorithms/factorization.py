import math

def factorize_number(number: int) -> list:
    """
    Функция производит факторизацию числа на простые множители.
    number: число, которое нужно факторизовать
    возвращает список простых множителей, на которые раскладывается число number.
    """
    factors = []
    divisor = 2
    while divisor <= math.sqrt(number):
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1:
        factors.append(number)
    return factors


if __name__ == '__main__':
    number = int(input())
    factors = factorize_number(number)
    print(" ".join(str(factor) for factor in factors))
