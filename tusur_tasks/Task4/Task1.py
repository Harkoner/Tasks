from random import randint


def task1(count: int, rand_list=[]):
    """
    Дано: 3 случайных числа.
    Задание: написать программу, которая будет вычислять среднее значение этих чисел.
    Пример: (52 + 56 + 60) / 3 = 56
    """
    i = 0
    sum = 0
    count_list = int(input('Type the count of numbers: '))
    while count_list > i:
        rand_list.append(randint(0, 100))
        i += 1
    for i in range(len(rand_list)):
        sum += rand_list[i]
    average = sum / count
    return f'#{count} Generated: {rand_list} result: {int(average)}'
