def task3(count: int, num=123):
    """
Дано: Число N = [1-9].
Задание: нужно написать программу, которая выведет последовательность 123..N
Пример:
 N = 3, результат: 123
 N = 9, результат: 123456789
 x = 1, результат: 1
    """
    num = int(input('Please type the number between 1 and 9: '))
    number = num
    answer = ''
    while number > 0:
        answer = answer + str(number)
        number = number - 1
    return f'#{count} number = {num}, result: "{int(answer[::-1])}"'