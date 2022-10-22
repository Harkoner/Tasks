from random import randint


def taskn():
    tasks = (Task1(), Task2(), Task3())
    print('For now, is ready for check 5 tasks'.center(50))
    while True:
            tasknumber = input('Please choose the number of task you are looking for:'.center(50))
            if tasknumber.isdigit():
                tasknumber = int(tasknumber)
                if tasknumber <= 5:
                    tasks[tasknumber - 1].start()
                else:
                    print('Choose the correct number'.center(50))
            elif tasknumber == 'esc':
                break
            else:
                print('Choose the correct number'.center(50))


class Task1:
    def start(self):
        while True:
            count = input('Type the count of numbers: ')
            if count.isdigit():
                count = int(count)
                randlist = []
                i = 0
                while count > i:
                    randlist.append(randint(0, 100))
                    i += 1
            else:
                print('Choose the correct number'.center(50))
            print('Bottom you can see the generated numbers:\n', randlist)
            sum = 0
            for i in range(len(randlist)):
                sum = randlist[i] + sum
            average = sum / count
            print('The average is: ', int(average))
            break


class Task2:
    def start(self):
        while True:
            x = randint(100, 200)
            y = randint(10, 99)
            print(f'Bottom you can see the generated numbers:\n{x} {y}\n')
            halving = x / y
            print(str(int(halving))+",", int((float(halving)-int(halving))*10))
            break


class Task3:
    def start(self):
        x = float(20.721)
        print('1)', '{:.2f}'.format(x))
        print('2)', int(x + (0.5 if (x - int(x)) > 0.5 else 0)))
        print('3)', '{:=011}'.format(x))


if __name__ == '__main__':
    taskn()
