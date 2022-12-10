def task1(count: int, some_number=123):

    """
    Задание:
    "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению.
    Давайте обучим компьютер.
    Вы должны написать программу, которая принимает положительное целое число и возвращает
    сл. значения.
    "Fizz Buzz", если число делится на 3 и 5;
    "Fizz", если число делится на 3;
    "Buzz", если число делится на 5;
    Число, как строку для остальных случаев.
    """
    some_number = input('Please type the positive number: ')
    some_number = int(some_number)
    devision3 = some_number % 3
    devision5 = some_number % 5
    answer = ''
    if devision3 == 0:
        answer = answer + 'Fizz'
    if devision5 == 0:
        if answer == '':
            answer = answer + 'Buzz'
        else:
            answer = answer + ' Buzz'
    if answer == '':
        return f'#{count} x = {some_number}, result: "{some_number}"'
    else:
        return f'#{count} x = {some_number}, result: "{answer}"'