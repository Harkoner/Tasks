def task2(count: int, number=123):
    """
    Задание:
    Дано: Число x.
    Задание: нужно написать программу, которая дает оценку заданному значению, используя следующие правила.
    если x нечетное, то это "Плохо"
    если x = [2, 5] и четное, то это "Неплохо"
    если x = [6, 20] и четное, то это "Так себе"
    если x > 20 и четное, то это "Отлично"
    """
    number = input('Please type any integer number: ')
    devision2 = int(number) % 2
    answer = ''
    if devision2 == 0:
        number = int(number)
        if number in range(2, 5):
            answer = 'Not Bad'
        if number in range(6, 20):
            answer = 'Weak'
        if number > 20:
            answer = 'Excellent'
    else:
        answer = 'Bad'
    return f'#{count} number = {number}, result: "{answer}"'