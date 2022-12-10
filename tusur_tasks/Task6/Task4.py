def task4(count: int,
          raw_list=[]):
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
    input_numbers = (input('please type the numbers in format "123 343 1 23": '))
    raw_list = [int(number) for number in input_numbers.split()]
    temp_elements = raw_list[:]
    temp_elements.sort()
    index_temp_elements = int(len(temp_elements) / 2)
    if len(temp_elements) % 2 == 0:
        return f'{count}) referenced: {raw_list} result: {(temp_elements[index_temp_elements] + temp_elements[index_temp_elements - 1]) / 2}'
    else:
        return f'{count}) referenced: {raw_list} result: {(temp_elements[index_temp_elements])}'