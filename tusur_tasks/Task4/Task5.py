def task5(count: int, number=123):
    """
    Дано: целое число (int).
    Задание: написать программу, которая будет инвертировать целое число. Если инвертированное число выходит за границы (32-bit integer)
    Пример:
    x = 123 -> 321
    x = -325 -> -523
    x = 0 -> 0
    x = 1563847412 -> 0
    """
    number = int(input('Please type any integer number: '))
    positive32bit = (2 ** 32) - 1
    negative32bit = (2 ** 32) * -1
    if int(number) > 0:
        number_re = str(number)[::-1]
    else:
        number_re = str(abs(number))[::-1]
        number_re = int(number_re) * -1
    if int(positive32bit) > int(number_re) > int(negative32bit):
        return f'#{count} Referenced: {number}, Result: {number_re}'
    else:
        return f'#{count} Referenced: {number}, Result: {0}'