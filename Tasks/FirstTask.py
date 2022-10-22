def taskn():
    tasks = (Task1(), Task2(), Task3(), Task4(), Task5())
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
#Task1
class Task1:
    def start(self):
        print('Task#1')
        print('Welcome to the python\n'
              'Lets get started!\n'
              'Please enter your First name\n')
        firstname = input()
        print('What is your last name?')
        secondname = input()
        print(f"Hello, {firstname.title()} {secondname.title()}!, you just delved into Python. Great start")


#Task2
class Task2:
    def picture(self):
        thickness = 5
        c = 'H'
        #Top Cone
        for i in range(thickness):
            print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))
        #Top Pillars
        for i in range(thickness+1):
            print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))
        #Middle Belt
        for i in range((thickness+1)//2):
            print((c*thickness*5).center(thickness*6))
        #Bottom Pillars
        for i in range(thickness+1):
            print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))
        #Bottom Cone
        for i in range(thickness):
            print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

    def start(self):
        print('Task#2')
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


"""
На самом деле не разобрался как задать область значений для answer1, чтобы он принимал только два значения
Чтобы вызвать проверку между y/n, но в остальном работает. 
Так же не совсем научился работать с самим "рисованием", выглядит как магия, даже если понимать как это работает
"""

#Task3
class Task3:
    def start(self):
        print('Task#3')
        input('Нажмите любую клавишу чтобы увидеть ответ')
        firstname = 'ivan'
        secondname = 'ivanovich'
        print('Hello', firstname.title(), secondname.title()+'!', 'You just delved into Python. Great start!')
        input('Нажмите любую клавишу чтобы продолжить')

#Task4
class Task4:
    def start(self):
        print('Task#4')
        from random import uniform
        amount = (uniform(100_000, 100_500))
        print(f"This is our random number {amount}")
        print('Do you wanna see the magic?')
        print('y/n')
        answer = input()
        while answer == 'y' or 'n':
            if answer == 'y':
                print(f"Lets format our numer into the money equivalent \nNew format: {amount} to {'{0:3,.3f}'.format(amount)}")
                break
            elif answer == 'n':
                print('All right, go next')
                break
            elif answer != 'y' or 'n':
                Task4.start(self)
                break
#Task5
class Task5:
    def start(self):
        """К сожалению я не совсем научился именно рисовать эти ковры, но попытался реализовать работу оператора"""
        print('Task#5')
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
                print('Choose the correct number1'.center(50))
        return
if __name__ == '__main__':
    taskn()
