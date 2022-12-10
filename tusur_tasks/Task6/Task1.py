def task1(count: int,
          raw_list=[]):
    """
    Дано: список (list) целых чисел (int).
    Задание: нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива.
    Пример:
    elements = [0, 1, 2, 3, 4, 5], результат: 30
    elements = [1, 3, 5], результат: 30
    elements = [] , результат: 0
    """
    input_numbers = (input('please type the numbers in format "123 343 1 23": '))
    raw_list = [int(number) for number in input_numbers.split()]
    if raw_list == []:
        return f'#{count} Generated list: {raw_list}; result: {0}'
    else:
        elements = raw_list[:]
        return f'#{count} Generated list: {raw_list}; result: {sum(elements[::2]) * elements[-1]}'
