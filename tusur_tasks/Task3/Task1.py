def task1(count: int, var='ivan ivanov'):
    """
    Дано: имя и фамилия.
    Задание: написать программу, которая будет приветствовать нового человека в мире Python. Текст приветсвия: Hello NAME SURNAME! You just delved into Python. Great start!
    Пример: Hello Ibrahim Petrov! You just delved into Python. Great start!
    """
    print('Please enter your First name')
    first_name = input()
    print('What is your last name?')
    second_name = input()
    return f"Hello, {first_name.title()} {second_name.title()}!, you just delved into Python. Great start"