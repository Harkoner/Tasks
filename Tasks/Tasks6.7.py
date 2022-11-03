from random import randint
import random


def task_n():  #Here is main func for selecting which task you wants to check
    tasks = (Task1(), Task2(), Task3())  #Here is variable which contains args which is our funcs of task
    tasks_count = len(tasks)
    print(f'For now, is ready for check {tasks_count} tasks'.center(50))
    while True:
        task_number = input('Please choose the number of task you are looking for:'.center(50))
        if task_number.isdigit():  #Check is inputed text is a number or not
            task_number = int(task_number)
            if task_number <= tasks_count:
                tasks[task_number - 1].start()  #script to start our choosen task
            else:
                print('Choose the correct number'.center(50))
        elif task_number == 'esc':  #extra func to exit the loop of choosing the tasks
            break
        else:
            print('Choose the correct number'.center(50))


class Task1:

    """
    Дано: список (list) целых чисел (int).
    Задание: нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива.
    Пример:
    elements = [0, 1, 2, 3, 4, 5], результат: 30
    elements = [1, 3, 5], результат: 30
    elements = [] , результат: 0
    """

    def start(self):
        print('Task#1 [-Junior]')
        elements = []
        i = randint(0, 15)
        tmp = i
        if i != 0:
            while i > 0:
                elements.append(randint(0, 9))
                i -= 1
            result = sum(elements[::2])
        else:
            result = 0
        result = result * tmp
        print(f'Generated list down here:\n{elements}')
        print(f'Sum: {result}')




"""
Интереса ради написал функцию каттера.
Которая должна перебирать все значения из списка list в котором хранятся числа в формате float
Которые необходимо ограничить конкретным количеством знаков после запятой которая хранится в аргументе n
Теоретически можно реализовать запрос у оператора на эти параметры, но для задания взято n = 4
"""
def cutter(list, n):
    for i, x in enumerate(list):
        cut = ''
        cut = cut + '{' + ':' + '.' + str(n) + 'f' + '}'
        a = float(cut.format(x))
        list[i] = a
    return list


# Task2
class Task2:

    """
    Дано: массив чисел (float или/и int).
    Задание: нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Если список пуст, то результат равен 0 (ноль).
    Числа с плавающей точкой представлены в компьютерах как двоичная дробь. Результат проверяется с точностью до третьего знака, как ±0.001
    Пример:
    elements = [1, 2, 3], результат: 2
    elements = [5, -5], результат: 30
    elements = [10.2, -2.2, 0, 1.1, 0.5], результат: 12.4
    elements = [] , результат: 0
    """


    def start(self):
        print('Task#2 [-Junior]')
        elements = []
        i = randint(0, 5)
        if i != 0:
            while i > 0:
                elements.append(random.uniform(0, 15.000))
                i -= 1
            result = max(elements) - min(elements)
        else:
            result = 0
        print('elements: ', cutter(elements, 4), 'result: ', '{0:.3f}'.format(result))


class Task3:

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

    def start(self):
        """undone"""




if __name__ == '__main__':
    task_n()
