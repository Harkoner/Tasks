from random import randint
import random
import string
import requests


def tests(num_task: 'Contains a number of func we want to test',
          count: 'contains a tech param',
          num_test: 'contains a number of tests',
          WORDS: 'type = list') -> 'Call a func: tasks[num_task](test object, count)':
    tasks = {
        1: task1,
        2: task2,
        3: task3,
        4: task4,
        5: task5,
    }
    if num_task == 1:
        return tasks[num_task]([randint(0, 20) for i in range(randint(0, 8))], count)
    if num_task == 2:
        return tasks[num_task]([random.uniform(-5.0, 15.0) for i in range(randint(0, 8))], count)
    if num_task == 3:
        return tasks[num_task]([randint(-20, 70) for i in range(5)], count)
    if num_task == 4:
        return tasks[num_task]([randint(0, 200) for i in range(randint(1, 7))], count)
    if num_task == 5:
        list_of_words = WORDS[:]
        text = ''.join([str(random.choice(list_of_words))[2:-1] + ' ' for x in range(randint(3, 7))])[:-1]
        return tasks[num_task](text, count)


def caller(num):
    if num == 1:
        return 'Task#1 [-Junior]'
    if num == 2:
        return 'Task#2 [-Junior]'
    if num == 3:
        return 'Task#3 [-Junior]'
    if num == 4:
        return 'Task#4 [Junior]'
    if num == 5:
        return 'Task#5 [+Junior]'


def start() -> 'Starting func':
    i = 0
    WORDS = []
    num = input('please type the number of task: ')
    if num != 'exit':
        num = int(num)
        test = input('Would you like to see multiple tests? [y/n]: ')
        num_test = 1
        if test == 'y':
            num_test = int(input('Type the number of tests you would like to see: '))
        if num == 5:
            word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
            response = requests.get(word_site)
            WORDS = response.content.splitlines()
        print(caller(num))
        while i < num_test:
            print(tests(num, i + 1, num_test, WORDS))
            i += 1
        start()


# task1
def task1(raw_list: 'Type = list',
          count: 'tech param') -> 'Started a task1 with num which is param of testing obj':
    """
    Дано: список (list) целых чисел (int).
    Задание: нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива.
    Пример:
    elements = [0, 1, 2, 3, 4, 5], результат: 30
    elements = [1, 3, 5], результат: 30
    elements = [] , результат: 0
    """
    if raw_list == []:
        return f'#{count} Generated list: {raw_list}; result: {0}'
    else:
        elements = raw_list[:]
        return f'#{count} Generated list: {raw_list}; result: even_index_list{elements[::2]}, Sum = {sum(elements[::2])}, devided by last number = {sum(elements[::2]) * elements[-1]}'


def cutter(list: 'type = list, contains an items with non sorted digits format',
           n: 'type = int, contains the number of digits after point') -> 'sorted list by param n':
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
def task2(raw_list, count):
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
    elements = raw_list[:]
    if elements != []:
        result = max(elements) - min(elements)
    else:
        result = 0
    return f'#{count} Elements: ' + str(cutter(elements, 4)) + ' result: ' + '{0:.3f}'.format(abs(result))


# Task3
def task3(elements, count):
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
    temp_elements.sort(key=abs)
    return f'#{count} ' + 'reference: {}, result: {}'.format(elements, temp_elements)


def task4(raw_list, count):
    """
    Дано: кортеж или список чисел.
    Задание: Медиана - это числовое значение, которое делит сортированый массив чисел на большую и меньшую половины.
    В сортированом массиве с нечетным числом элементов медиана - это число в середине массива.
    Для массива с четным числом элементов, где нет одного элемента точно посередине,
    медиана - это среднее значение двух чисел, находящихся в середине массива.
    В этой задаче дан непустой массив натуральных чисел.
    Вам необходимо найти медиану данного массива.
    Пример:
    elements = [1, 2, 3, 4, 5], результат: 3
    elements = [3, 1, 2, 5, 3], результат: 3
    elements = [1, 300, 2, 200, 1], результат: 2
    elements = [3, 6, 20, 99, 10, 15], результат: 12.5
    """
    temp_elements = raw_list[:]
    temp_elements.sort()
    index_temp_elements = int(len(temp_elements) / 2)
    if len(temp_elements) % 2 == 0:
        return f'{count}) referenced: {raw_list} sorted: {temp_elements} result: {(temp_elements[index_temp_elements] + temp_elements[index_temp_elements - 1]) / 2}'
    else:
        return f'{count}) referenced: {raw_list} sorted: {temp_elements} result: {(temp_elements[index_temp_elements])}'


# : parcing (почитать что это)

def task5(text, count):
    """
    Дано: текст, как строка (str).
    Задание: Наши Роботы никогда не упускают возможности, чтобы улучшить свои навыки в лингвистике. Сейчас они изучают английский алфавит и что с этим делать.
    Алфавит разделен на гласные и согласные буквы (да, мы разделили буквы, а не звуки).
    Гласные -- A E I O U Y
    Согласные -- B C D F G H J K L M N P Q R S T V W X Z
    Дан текст с разными словами и/или числами, которые разделены пробелами и знаками пунктуации.
    Числа не считаются за слова (также как и смесь букв и цифр).
    Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными (полосатые слова),
    то есть в таких словах нет двух гласных или двух согласных букв подряд.
    Слова состоящие из одной буквы - не "полосатые" (не считайте их).
    Регистр букв не имеет значения.
    Пример:
    text = "My name is ...", результат: 3
    text = "Hello world", результат: 0
    text = "A quantity of striped words.", результат: 1
    text = "Dog,cat,mouse,bird.Human.", результат: 3
    """
    vowels = 'aAeEiIoOuUyY'
    consonant = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZ'
    i = 0  # num of liter
    answer = 0
    final_answer = 0
    text_list = text.split()
    for words in text_list:
        if len(words) != 1:
            while i + 1 < len(words):
                if words[i] in vowels and words[i + 1] in vowels:
                    answer += 1
                elif words[i] in consonant and words[i + 1] in consonant:
                    answer += 1
                i += 1
            i = 0
            if answer == 0:
                final_answer += 1
            answer = 0
    return f'#{count} referenced: "{text}" result: {final_answer}'


if __name__ == '__main__':
    start()

# Questions
"""
1) Глобальные переменные - добро или зло?
2) Функции в одну строку - это плохо или можно если возможно?
3) В каждом задании учет правильность ввода скажем если в задании предусмотрен ввод списка или числа, а мы подаем строку или другой тип данных
4) Плодить много переменных в функциях но реализовать программу или стоит все же использовать ООП и не заниматься ерундой?
5) Что лучше? Решать много простых заданий и тратить по 5-10 минут на каждое, или делать 3-5 сложны заданий но каждое по 1-1.5 часа?
6) Какие основные дополнения к питону стоит изучать? Тот же Django, Какие есть достойные аналоги?
7) Питон часто используется для Data Science, так вот, какую литературу стоит посмотреть если хочешь работать в этом направлении?
   (Имеется в виду по мимо базы самого Питона)
"""
