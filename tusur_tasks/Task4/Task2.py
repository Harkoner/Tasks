def task2(count: int, raw_list=[]):
    """
    Дано: 2 случайных числа.
    Задание: написать программу, которая будет печать результат целочисленного деления этих чисел, а также остаток от деления первого от второго.
    Пример:
     x = 177 и y = 10
    Результат:
     17, 7
    """
    raw_list = [int(input('Please input first number: ')), int(input('Please input second number: '))]
    halving = raw_list[0] / raw_list[1]
    halving_int = int(halving)
    rest = int((float(halving) - halving_int) * 10)
    integer_number = halving_int
    return f'#{count} Referenced: {raw_list}, result: {integer_number}, {rest}'
