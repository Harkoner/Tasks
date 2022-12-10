from random import randint


def double_odd(data):
    """
    3. Удвоенные нечетные.
    Дано: n.
    Задание: нужно получить список "удвоенных" нечетных чисел от 0 до n.
    Пример:
    n = 5, результат: [2, 6]
    """
    return [x * 2 for x in range(data) if x % 2 == 1]


def double_odd_view(data):
    answer = double_odd(data)
    return f'n = {data}, result {answer}'


if __name__ == '__main__':
    data = randint(1, 10)
    print(double_odd_view(data))
