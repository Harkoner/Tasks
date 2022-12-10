from random import randint


def get_non_unic(data: list):
    """
Дано: непустой массив целых чисел.
Задание: нужно получить массив, состоящий только из неуникальных элементов данного массива.
Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз).
Для решения этой задачи не меняйте оригинальный порядок элементов. Пример: [1, 2, 3, 1, 3],
где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].
Пример
[1, 2, 3, 1, 3], результат: [1, 3, 1, 3]
[1, 2, 3, 4, 5], результат: []
[5, 5, 5, 5, 5], результат: [5, 5, 5, 5, 5]
[10, 9, 10, 10, 9, 8], результат: [10, 9, 10, 10, 9]
    """
    data1 = data[:]
    result_list = []
    for element in data1:
        if data1.count(element) > 1:
            result_list.append(element)
    return result_list


def get_non_unic_view(data):
    answer = get_non_unic(data)
    return f'{data}, result: {answer}'


def data_generator():
    return [randint(1, 10) for x in range(6)]


if __name__ == '__main__':
    # data = [10, 9, 10, 10, 9, 8]
    data = data_generator()
    print(get_non_unic_view(data))
