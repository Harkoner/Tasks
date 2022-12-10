def task4(count: int, number=123):
    """
    Дано: целое число (int).
    Задание: написать программу, которая будет инвертировать целое число
    Пример:
    x = 123 -> 321
    x = -325 -> -523
    x = 0 -> 0
    """
    number = input('Please type any integer number: ')
    if int(number) > 0:
        number_replic = str(number)[::-1]  # inverting the number which is currently string
    else:
        number_replic = int(
            number) * -1  # Now we said that our x is now integer and we wants to invert them to positive for correct inverting string then
        number_replic = str(number_replic)[::-1]
        number_replic = int(number_replic) * -1  # Just to put back minus for a number, but x still have format str.
    return f'#{count} Referenced: {number}, Result: {number_replic}'
