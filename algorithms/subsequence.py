def subsequence(sub: str, sequence: str) -> bool:
    """
    Функция проверяет, является ли строка sub подпоследовательностью строки sequence.
    sub: строка, которую нужно проверить на подпоследовательность.
    sequence: строка, в которой нужно найти подпоследовательность.

    Функция возвращает:
    True, если sub является подпоследовательностью sequence, иначе False.
    """
    sub_index = 0
    for seq_index in range(len(sequence)):
        if sub_index == len(sub):
            break
        if sub[sub_index] == sequence[seq_index]:
            sub_index += 1
    return sub_index == len(sub)

if __name__ == '__main__':
    sub = input().strip()
    sequence = input().strip()
    print(subsequence(sub, sequence))
