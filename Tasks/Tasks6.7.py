from random import randint
import random


def tests(num_task):
    if num_task == 1:
        return tasks123[num_task](randint(5, 15))
    if num_task == 2:
        return tasks123[num_task](randint(5, 15))
    if num_task == 3:
        test_list = []
        for x in range(5):
            test_list.append(randint(-20, 70))
        return tasks123[num_task](test_list)


def caller(num):
    if num == 1:
        return 'Task#1 [-Junior]'
    if num == 2:
        return 'Task#2 [-Junior]'
    if num == 3:
        return 'Task#3 [-Junior]'


def start():
    i = 0
    num = int(input('please type the number of task: '))
    num_test = int(input('please type the number: '))
    print(caller(num))
    while i < num_test:
        print(tests(num))
        i += 1
    start()


# task1
def task1(num):
    """
    Дано: список (list) целых чисел (int).
    Задание: нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива.
    Пример:
    elements = [0, 1, 2, 3, 4, 5], результат: 30
    elements = [1, 3, 5], результат: 30
    elements = [] , результат: 0
    """
    elements = []
    i = randint(0, int(num))
    tmp = i
    if i != 0:
        while i > 0:
            elements.append(randint(0, 9))
            i -= 1
        result = sum(elements[::2])
    else:
        result = 0
    result = result * tmp
    return f'Generated list: {elements}; {result = }'


def cutter(list, n):
    """
    Интереса ради написал функцию каттера.
    Которая должна перебирать все значения из списка list в котором хранятся числа в формате float
    Которые необходимо ограничить конкретным количеством знаков после запятой которая хранится в аргументе n
    Теоретически можно реализовать запрос у оператора на эти параметры, но для задания взято n = 4
    """
    for i, x in enumerate(list):
        cut = '{' + ':' + '.' + str(n) + 'f' + '}'
        tmp = float(cut.format(x))
        list[i] = tmp
    return list


# Task2
def task2(num):
    """
    Дано: массив чисел (float или/и int).
    Задание: нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Если список пуст, то результат равен 0 (ноль).
    Числа с плавающей точкой представлены в компьютерах как двоичная дробь. Результат проверяется с точностью до третьего знака, как ±0.001
    Пример:
    elements = [1, 2, 3], результат: 2
    elements = [5, -5], результат: 10
    elements = [10.2, -2.2, 0, 1.1, 0.5], результат: 12.4
    elements = [] , результат: 0
    """
    elements = []
    i = randint(0, int(num))
    if i != 0:
        while i > 0:
            elements.append(random.uniform(0, 15.0))
            i -= 1
        result = max(elements) - min(elements)
        if result < 0:
            result = result * -1
    else:
        result = 0
    return 'elements: ' + str(cutter(elements, 4)) + ' result: ' + '{0:.3f}'.format(result)


# Task3
def task3(elements):
    """
    Дано: кортеж (tuple) чисел.
    Задание: необходимо отсортировать их, но отсортировать на основе абсолютных значений в возрастающем порядке.
    Для примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим образом (-5, 10, 15, -20).
    Ваша функция должна возвращать список (list) или кортеж (tuple).
    Пример:
    elements = (-20, -5, 10, 15), результат: [-5, 10, 15, -20]
    elements = (1, 2, 3, 0), результат: [0, 1, 2, 3]
    elements = (-1, -2, -3, 0), результат: [0, -1, -2, -3]
    """
    temp_elements = elements[:]
    for x in temp_elements:
        if x < 0:
            temp_elements[temp_elements.index(x)] = x * -1
    temp_elements.sort()
    for y in elements:
        if y < 0:
            temp_elements[temp_elements.index(y * -1)] = temp_elements[temp_elements.index(y * -1)] * -1
    return 'reference: {}, result: {}'.format(elements, temp_elements)


tasks123 = {
        1: task1,
        2: task2,
        3: task3
        # '4': task4(),
        # '5': task5(),
        # '6': task6()
    }
# tests = {
#         1: '5',
#         2: '5'
#     }


if __name__ == '__main__':
    start()
