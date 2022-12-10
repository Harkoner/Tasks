def task6(count: int, value=100500):
    """
    Дано: целое число.
    Задание: написать программу, которая перемножит все цифры заданного числа (0 - исключить).
    Примеры: 1) value = 123405, результат = 120 2) value = 999, результат = 729 3) value = 1000, результат = 1 4) value = 1111, результат = 1
    """

    def calc(value):
        count_value = len(str(value))
        i = 0
        answer = 1
        while i < count_value:
            iter_current_value = int(str(value)[i])
            current_value = iter_current_value
            if current_value != 0:  # sorting our numbers by iter but except 0
                answer = current_value * int(answer)  # Making math as it asked
            i += 1
        return f'#{count} Number: {value}, Result: {answer}'
    value = input('Please type any number: ')
    return calc(value)
