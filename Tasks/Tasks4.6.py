from random import randint


def task_n():
    tasks = (Task1(), Task2(), Task3(), Task4(), Task5())
    print('For now, is ready for check 5 tasks'.center(50))
    while True:
        task_number = input('Please choose the number of task you are looking for:'.center(50))
        if task_number.isdigit():
            task_number = int(task_number)
            if task_number <= 5:
                tasks[task_number - 1].start()
            else:
                print('Choose the correct number'.center(50))
        elif task_number == 'esc':
            break
        else:
            print('Choose the correct number'.center(50))


class Task1:
    def start(self):
        print('Task#1 [-Junior]')
        while True:
            count = input('Type the count of numbers: ')
            if count.isdigit():
                count = int(count)
                rand_list = []
                i = 0
                while count > i:
                    rand_list.append(randint(0, 100))
                    i += 1
            else:
                print('Choose the correct number'.center(50))
            print('Bottom you can see the generated numbers:\n', rand_list)
            sum = 0
            for i in range(len(rand_list)):
                sum = rand_list[i] + sum
            average = sum / count
            print('The average is: ', int(average))
            break


class Task2:
    def start(self):
        print('Task#2 [-Junior]')
        while True:
            x = randint(100, 200)
            y = randint(10, 99)
            print(f'Bottom you can see the generated numbers:\n{x} {y}\n')
            halving = x / y
            print(str(int(halving))+",", int((float(halving)-int(halving))*10))
            break


class Task3:
    def start(self):
        print('Task#3 [-Junior]')
        x = float(20.721)
        print('1)', '{:.2f}'.format(x))
        print('2)', int(x + (0.5 if (x - int(x)) > 0.5 else 0)))
        print('3)', '{:=011}'.format(x))


class Task4:
    def start(self):
        print('Task#4 [Junior]')
        x = input('Please type any integer number: ')
        if int(x) > 0:
            x = x[::-1]
        else:
            x = int(x) * -1
            x = str(x)[::-1]
            x = int(x) * -1
        print(x)


class Task5:
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
