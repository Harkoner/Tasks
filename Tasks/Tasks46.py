from random import randint


def task1(count, manual=False, rand_list=[]):
    """
    Дано: 3 случайных числа.
    Задание: написать программу, которая будет вычислять среднее значение этих чисел.
    Пример: (52 + 56 + 60) / 3 = 56
    """
    i = 0
    sum = 0
    if manual:
        count = int(input('Type the count of numbers: '))
        while count > i:
            rand_list.append(randint(0, 100))
            i += 1
    for i in range(len(rand_list)):
        sum += rand_list[i]
    average = sum / count
    return f'#{count} Generated: {rand_list} result: {int(average)}'


def task2(count, manual=False, raw_list=[]):
    """
    Дано: 2 случайных числа.
    Задание: написать программу, которая будет печать результат целочисленного деления этих чисел, а также остаток от деления первого от второго.
    Пример:
     x = 177 и y = 10
    Результат:
     17, 7
    """
    if manual:
        raw_list = [int(input('Please input first number: ')), int(input('Please input second number: '))]
    halving = raw_list[0] / raw_list[1]
    halving_int = int(halving)
    rest = int((float(halving) - halving_int) * 10)
    integer_number = halving_int
    return f'#{count} Referenced: {raw_list}, result: {integer_number}, {rest}'


def task3(count, manual=False, number=123.123):
    """
    Дано: число с плавающей точкой.
    Задание: написать программу, которая будет округлять заданное число:
    2-х знаков после запятой;
    до целого;
    дополнять слева столько нулей, сколько не хватает числу до 11 знаков.
    Пример:
    x = 14.721
    14.72
    15
    0000014.721
    """
    if manual:
        number = float(input('Please type the float number: '))
    float_number = '{:.2f}'.format(number)
    int_number = int(number + (0.5 if (number - int(number)) > 0.5 else 0))
    number = '{:.3f}'.format(number)
    null_float_number = '{:=011}'.format(float(number))
    return f'#{count} Referece: {number}, 1) {float_number}, 2) {int_number}, 3) {null_float_number}'


def task4(count, manual=False, number=123):
    """
    Дано: целое число (int).
    Задание: написать программу, которая будет инвертировать целое число
    Пример:
    x = 123 -> 321
    x = -325 -> -523
    x = 0 -> 0
    """
    if manual:
        number = input('Please type any integer number: ')
    if int(number) > 0:
        number_replic = str(number)[::-1]  # inverting the number which is currently string
    else:
        number_replic = int(number) * -1  # Now we said that our x is now integer and we wants to invert them to positive for correct inverting string then
        number_replic = str(number_replic)[::-1]
        number_replic = int(number_replic) * -1  # Just to put back minus for a number, but x still have format str.
    return f'#{count} Referenced: {number}, Result: {number_replic}'


def task5(count, manual=False, number=123):
    """
    Дано: целое число (int).
    Задание: написать программу, которая будет инвертировать целое число. Если инвертированное число выходит за границы (32-bit integer)
    Пример:
    x = 123 -> 321
    x = -325 -> -523
    x = 0 -> 0
    x = 1563847412 -> 0
    """
    if manual:
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


if __name__ == '__main__':
    task_n()
