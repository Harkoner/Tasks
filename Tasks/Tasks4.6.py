from random import randint


def task_n():  #Here is main func for selecting which task you wants to check
    tasks = (Task1(), Task2(), Task3(), Task4(), Task5())  #Here is variable which contains args which is our funcs of task
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


class Task1:
    """
    Дано: 3 случайных числа.
    Задание: написать программу, которая будет вычислять среднее значение этих чисел.
    Пример: (52 + 56 + 60) / 3 = 56
    """
    def start(self):
        print('Task#1 [-Junior]')
        while True:
            count = input('Type the count of numbers: ')  #For testing is script work or not we are asking for count of random numbers
            rand_list = []
            i = 0
            sum = 0
            if count.isdigit():
                count = int(count)
                while count > i:
                    rand_list.append(randint(0, 100))
                    i += 1
            else:
                print('Choose the correct number'.center(50))
            print('Bottom you can see the generated numbers:\n', rand_list)
            for i in range(len(rand_list)):
                sum += rand_list[i]
            average = sum / count
            print('The average is: ', int(average))
            break


class Task2:
    """
    Дано: 2 случайных числа.
    Задание: написать программу, которая будет печать результат целочисленного деления этих чисел, а также остаток от деления первого от второго.
    Пример:
     x = 177 и y = 10
    Результат:
     17, 7
    """
    def start(self):
        print('Task#2 [-Junior]')
        while True:
            x = randint(100, 200)
            y = randint(10, 99)
            print(f'Bottom you can see the generated numbers:\n{x} {y}\n')
            halving = x / y
            print(str(int(halving))+",", int((float(halving)-int(halving))*10))  #it works, not how suppose to be, but it works
            break


class Task3:
    """
    Дано: число с плавающей точкой.
    Задание: написать программу, которая будет округлять заданное число:
    2-х знаков после запятой;
    до целого;
    дополнять слева столько нулей, сколько не хватает числу до 11 знаков.
    Пример:
    x = 14.721
    14.72
    15
    0000014.721
    """
    def start(self):
        print('Task#3 [-Junior]')
        x = float(20.721)
        print('1)', '{:.2f}'.format(x))
        print('2)', int(x + (0.5 if (x - int(x)) > 0.5 else 0)))
        print('3)', '{:=011}'.format(x))


class Task4:
    """
    Дано: целое число (int).
    Задание: написать программу, которая будет инвертировать целое число
    Пример:
    x = 123 -> 321
    x = -325 -> -523
    x = 0 -> 0
    """
    def start(self):
        print('Task#4 [Junior]')
        x = input('Please type any integer number: ')
        if int(x) > 0:
            x = x[::-1]  #inverting the number which is currently string
        else:
            x = int(x) * -1  #Now we said that our x is now integer and we wants to invert them to positive for correct inverting string then
            x = str(x)[::-1]
            x = int(x) * -1  #Just to put back minus for a number, but x still have format str.
        print(x)


class Task5:
    """
    Дано: целое число (int).
    Задание: написать программу, которая будет инвертировать целое число. Если инвертированное число выходит за границы (32-bit integer)
    Пример:
    x = 123 -> 321
    x = -325 -> -523
    x = 0 -> 0
    x = 1563847412 -> 0
    """
    def start(self):
        print('Task #5 [Junior+]')
        x = input('Please type any integer number: ')
        positive32bit = (2 ** 32) - 1
        negative32bit = (2 ** 32) * -1
        if int(x) > 0:
            x = x[::-1]
        else:
            x = int(x) * -1
            x = str(x)[::-1]
            x = int(x) * -1
        if int(positive32bit) < int(x) < int(negative32bit):
            print(x)
        else:
            print(0)


if __name__ == '__main__':
    task_n()
