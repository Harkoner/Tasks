"""
    Дано: натуральное число N.
    Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.
    Пример:
    123, результат: [3, 2, 1]
"""

from random import randint


def get_list(number):
    return f'{number}, result: {[int(x) for x in str(number)][::-1]}'


if __name__ == '__main__':
    print(get_list(randint(100, 200)))
