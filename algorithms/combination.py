def get_combinations(digits: str, letters: dict, current: str, result: list):
    """
    Функция генерирует все возможные комбинации букв, которые можно набрать
    на клавиатуре старых мобильных телефонов по заданной последовательности цифр.

    digits: последовательность цифр, для которой нужно найти все комбинации букв.
    letters: словарь, связывающий цифры с наборами букв на клавиатуре телефона.
    current: текущая комбинация букв (по умолчанию пустая строка).
    result: список для хранения всех сгенерированных комбинаций (по умолчанию пустой список).
    """
    if len(digits) == 0:
        result.append(current)
        return
    # Получаем первую цифру и оставшуюся часть строки
    first_digit = digits[0]
    rest_digits = digits[1:]
    # Генерируем все возможные буквы для данной цифры
    for letter in letters[first_digit]:
        # Вызываем функцию рекурсивно для оставшейся части строки
        get_combinations(rest_digits, letters, current + letter, result)

if __name__ == '__main__':
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    digits = input().strip()
    result = []
    get_combinations(digits, letters, '', result)
    print(' '.join(result))
