def task3(count: int, text='hello world'):
    """
    Дано: текст любой длины.
    Задание: написать программу, которая выведет заголовок, используя заданный текст. Подсказка используйте метод title.
    Пример: text = 'hello world'; результат = Hello World
    """
    # text = (input('please type your name in format "ivan ivanovich": '))
    return f'#{count} Hello, {text.title()}!, You just delved into Python. Great start!'