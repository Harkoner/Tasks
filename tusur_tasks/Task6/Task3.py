def task3(count: int):
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
    input_numbers = (input('please type the numbers in format "123 343 1 23": '))
    elements = [int(number) for number in input_numbers.split()]
    temp_elements = elements[:]
    temp_elements.sort(key=abs)
    return f'#{count} reference: {elements}, result: {temp_elements}'

if __name__ == '__main__':
    print(task3(1))