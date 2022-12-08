import settings


def task1(count: int, var='ivan ivanov'):
    """
    Дано: имя и фамилия.
    Задание: написать программу, которая будет приветствовать нового человека в мире Python. Текст приветсвия: Hello NAME SURNAME! You just delved into Python. Great start!
    Пример: Hello Ibrahim Petrov! You just delved into Python. Great start!
    """
    if settings.Settings().manual == False:
        first_name = 'ivan'
        second_name = 'ivanov'
        return f"#{count} Hello, {var.title()}!, you just delved into Python. Great start"
    else:
        print('Please enter your First name')
        first_name = input()
        print('What is your last name?')
        second_name = input()
        return f"Hello, {first_name.title()} {second_name.title()}!, you just delved into Python. Great start"


# Task2
def task2(*args):
    """
    Дано: маркер (символ) и толщина фигуры.
    Задание: написать программу, которая будет отображать заданную фигуру.
    Пример: Маркер = H, толщина 5.
    """

    def picture():
        thickness = 5
        c = 'H'
        # Top Cone
        for i in range(thickness):
            print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
        # Top Pillars
        for i in range(thickness + 1):
            print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        # Middle Belt
        for i in range((thickness + 1) // 2):
            print((c * thickness * 5).center(thickness * 6))
        # Bottom Pillars
        for i in range(thickness + 1):
            print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        # Bottom Cone
        for i in range(thickness):
            print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
                thickness * 6))
        return 'Thanks for using our service!'

    return picture()


# Task3
def task3(count: int, text='hello world'):
    """
    Дано: текст любой длины.
    Задание: написать программу, которая выведет заголовок, используя заданный текст. Подсказка используйте метод title.
    Пример: text = 'hello world'; результат = Hello World
    """
    if settings.Settings().manual:
        text = (input('please type your name in format "ivan ivanovich": '))
    return f'#{count} Hello, {text.title()}!, You just delved into Python. Great start!'


# Task4
def task4(count: int, var=100500.345):
    """
    Дано: денежная сумма (amount > 0).
    Задание: написать программу, которая распечатает число в принятом денежном формате XXX,XXX.XX.
    Пример: amount = 100500.157; результат = 100,500.16
    """
    if settings.Settings().manual:
        var = float(input('Type the float number: '))
    return f"#{count} Number: {var}, Result: {'{0:3,.3f}'.format(var)}"


# Task5
def task5(count: int, var=100500.345):
    """
    Дизайнер составил шаблон домашних ковриков. Для массового выпуска ковриков ему нужно уметь быстро составлять макет произвольного размера.
    Известно, что длина коврика всегда больше в 3 раза чем его ширина (W = 3 * H).
    Дано: ширина коврика.
    Задание: написать программу, которая будет составлять макет коврика для его дальнейшего производства.
    """

    def carpet(height_number):
        if height_number.isdigit():
            height = int(height_number)
            if height in range(10, 100, 1):
                width = height * 3
                print(f"Your carpet settings is {height:} and {width:}\n")
                print('Lets make them!'.center(width))
                for stick_count in range(1, height, 2):
                    print(('.|.' * stick_count).center(width, '-'))
                print('Presented by Nikolay Kriger'.center(width, '-'))
                for stick_count in range(height - 2, 0, -2):
                    print(('.|.' * stick_count).center(width, '-'))
            elif height not in range(10, 100, 1):
                print('Choose the correct number'.center(50))
                return task5(count, manual, ' ')
        else:
            print('Please use only numbers between 10 and 99!'.center(50))
            return task5(count, manual, ' ')
        return 'Thank you for using our service!'

    if settings.Settings().manual:
        var = input("Please enter the height between 10 and 99: ")
    return carpet(var)


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

    if settings.Settings().manual:
        value = input('Please type any number: ')
    return calc(value)


if __name__ == '__main__':
    print('Welcome to the Tasks3.6\n'
          'Lets make our setup real quick')
    settings()
