def task_n():  #Here is main func for selecting which task you wants to check
    tasks = (Task1(), Task2(), Task3(), Task4(), Task5(), Task6())  #Here is variable which contains args which is our funcs of task
    tasks_count = len(tasks)
    print(f'For now, is ready for check {tasks_count} tasks'.center(50))
    while True:
        task_number = input('Please choose the number of task you are looking for:'.center(50))
        if task_number.isdigit():  #Check is inputed text is a number or not
            task_number = int(task_number)
            if task_number <= tasks_count:
                tasks[task_number - 1].start()  #script to start our choosen task
            else:
                print('Choose the correct number'.center(50))
        elif task_number == 'esc':  #extra func to exit the loop of choosing the tasks
            break
        else:
            print('Choose the correct number'.center(50))


# Task1
class Task1:
    """
    Дано: имя и фамилия.
    Задание: написать программу, которая будет приветствовать нового человека в мире Python. Текст приветсвия: Hello NAME SURNAME! You just delved into Python. Great start!
    Пример: Hello Ibrahim Petrov! You just delved into Python. Great start!
    """
    def start(self):
        print('Task#1 [-Junior]')
        print('Welcome to the python\n'
              'Lets get started!\n'
              'Please enter your First name\n')
        first_name = input()
        print('What is your last name?')
        second_name = input()
        print(f"Hello, {first_name.title()} {second_name.title()}!, you just delved into Python. Great start")


# Task2
class Task2:
    """
    Дано: маркер (символ) и толщина фигуры.
    Задание: написать программу, которая будет отображать заданную фигуру.
    Пример: Маркер = H, толщина 5.
    """
    def picture(self):
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

    def start(self):
        print('Task#2 [-Junior]')
        print('Do you want to see a picture?')
        print('y/n')
        answer = input()
        while answer == 'y' or 'n':
            if answer == 'y':
                self.picture()
                break
            elif answer == 'n':
                print('All right, go next')
                break
            elif answer != 'y' or 'n':
                Task2.start(self)
                break


# Task3
class Task3:
    """
    Дано: текст любой длины.
    Задание: написать программу, которая выведет заголовок, используя заданный текст. Подсказка используйте метод title.
    Пример: text = 'hello world'; результат = Hello World
    """
    def start(self):
        print('Task#3 [-Junior]')
        input('Нажмите любую клавишу чтобы увидеть ответ')
        first_name = 'ivan'
        second_name = 'ivanovich'
        print('Hello', first_name.title(), second_name.title() + '!', 'You just delved into Python. Great start!')
        input('Нажмите любую клавишу чтобы продолжить')


# Task4
class Task4:
    """
    Дано: денежная сумма (amount > 0).
    Задание: написать программу, которая распечатает число в принятом денежном формате XXX,XXX.XX.
    Пример: amount = 100500.157; результат = 100,500.16
    """
    def start(self):
        print('Task#4 [-Junior]')
        from random import uniform
        amount = (uniform(100_000, 100_500))
        print(f"This is our random number {amount}")
        print('Do you wanna see the magic?')
        print('y/n')
        answer = input()
        while answer == 'y' or 'n':
            if answer == 'y':
                print(
                    f"Lets format our numer into the money equivalent \nNew format: {amount} to {'{0:3,.3f}'.format(amount)}")
                break
            elif answer == 'n':
                print('All right, go next')
                break
            elif answer != 'y' or 'n':
                Task4.start(self)
                break


# Task5
class Task5:
    """
    Дизайнер составил шаблон домашних ковриков. Для массового выпуска ковриков ему нужно уметь быстро составлять макет произвольного размера.
    Известно, что длина коврика всегда больше в 3 раза чем его ширина (W = 3 * H).
    Дано: ширина коврика.
    Задание: написать программу, которая будет составлять макет коврика для его дальнейшего производства.
    """
    def start(self):
        print('Task#5 [Junior]')
        print('Welcome to the carpet calculator.')
        while True:
            height_number = input("Please enter the height between 10 and 99: ")
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
                    break
                elif height not in range(10, 100, 1):
                    print('Choose the correct number'.center(50))
            else:
                print('Choose the correct number'.center(50))
        return


class Task6:
    """
    Дано: целое число.
    Задание: написать программу, которая перемножит все цифры заданного числа (0 - исключить).
    Примеры: 1) value = 123405, результат = 120 2) value = 999, результат = 729 3) value = 1000, результат = 1 4) value = 1111, результат = 1
    """
    def start(self):
        print('Task#6 [Junior+]')
        print('Welcome to the Strange Calculator, like a SC (bad joke)')
        value = input('Please type any number: ')
        if value.isdigit():
            count_value = len(str(value))
            i = 0
            answer = 1
            while i < count_value:
                if int(value[i]) != 0:  #sorting our numbers by iter but except 0
                    answer = int(value[i]) * int(answer)  #Making math as it asked
                i += 1
            print(f'The answer is: {answer}')
            input('Enter to continue')
        else:
            print('Choose the correct number'.center(50))


if __name__ == '__main__':
    task_n()
