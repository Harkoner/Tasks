def cutter(list: list[float],
           n: int):
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
def task2(count: int,
          raw_list=[]):
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
    input_numbers = (input('please type the numbers in format "123 343 1 23": '))
    raw_list = [int(number) for number in input_numbers.split()]
    elements = raw_list[:]
    if elements != []:
        result = max(elements) - min(elements)
    else:
        result = 0
    return f'#{count} Elements: ' + str(cutter(elements, 4)) + ' result: ' + '{0:.3f}'.format(abs(result))
