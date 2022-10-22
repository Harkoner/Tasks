#Task1
def task1():
    print('Task#1')
    print('Welcome to the python\n'
          'Lets get started!\n'
          'Please enter your First name\n')
    global firstname
    firstname = input()
    print('What is your last name?')
    global secondname
    secondname = input()
    print(f"Hello, {firstname.title()} {secondname.title()}!, you just delved into Python. Great start")


#Task2
def picture():
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

def task2():
    print('Task#2')
    print('Do you want to see a picture?')
    print('y/n')
    answer1 = input()
    if answer1 == 'y':
        picture()
    else:
        print('All right, go next')

"""
На самом деле не разобрался как задать область значений для answer1, чтобы он принимал только два значения
Чтобы вызвать проверку между y/n, но в остальном работает. 
Так же не совсем научился работать с самим "рисованием", выглядит как магия, даже если понимать как это
работает
"""

#Task3
def task3():
    print('Task#3')
    input('Нажмите любую клавишу чтобы увидеть ответ')
    firstname = 'Ivan'
    secondname = 'Ivanovich'
    print('Hello', firstname.title(), secondname.title()+'!', 'You just delved into Python. Great start!')
    input('Нажмите любую клавишу чтобы продолжить')

#Task4
def task4():
    print('Task#4')
    from random import uniform
    amount = (uniform(100_000, 100_500))
    print(f"This is our random numer {amount}")
    print('Do you wanna see the magic?')
    print('y/n')
    answer2 = input()
    if answer2 == 'y':
          print(f"Lets format our numer into the money equivalent \nNew format: {'{0:3,.3f}'.format(amount)}")
    else:
          print('All right, go next for the Task#5')

#Task5
def task5():
    """К сожалению я не совсем научился именно рисовать эти ковры, но попытался реализовать работу оператора"""

    print('Task#5')
    print('Welcome to the carpet calculator.')
    height_number = input("Please enter the height between 10 and 99: ")
    height = int(height_number)
    if height >= 10:
        width = height * 3
        print(f"Your carpet settings is {height:} and {width:}\n")
        print('Lets make them!'.center(width))
        for stick_count in range(1, height, 2):
            print(('.|.' * stick_count).center(width, '-'))
        print('Presented by Nikolay Kriger'.center(width, '-'))
        for stick_count in range(height-2, 0, -2):
            print(('.|.' * stick_count).center(width, '-'))
    else:
        height_number = input("Please try again and enter the height between 10 and 99: ")
        height = int(height_number)
        if height >= 10:
            width = height * 3
            print(f"Your carpet settings is {height:} and {width:}\n")
            print('Lets make them!'.center(width))
            for stick_count in range(1, height, 2):
                print(('.|.' * stick_count).center(width, '-'))
            print('Presented by Nikolay Kriger'.center(width, '-'))
            for stick_count in range(height - 2, 0, -2):
                print(('.|.' * stick_count).center(width, '-'))
        else:
            print('We are sorry but we cannot make this size of carpet.')
    print('Thank you for using our service!')

def taskn():
    print('For now, is ready for check 5 tasks'.center(50))
    tasknumber = input('Please choose the number of task you are looking for:'.center(50))
    while tasknumber < '6':
        if tasknumber == '1':
            task1()
            tasknumber = input('choose another number of task: ')
        elif tasknumber == '2':
            task2()
            tasknumber = input('choose another number of task: ')
        elif tasknumber == '3':
            task3()
            tasknumber = input('choose another number of task: ')
        elif tasknumber == '4':
            task4()
            tasknumber = input('choose another number of task: ')
        elif tasknumber == '5':
            task5()
            tasknumber = input('choose another number of task: ')
    else:
        return("We are sorry but this task isn't complited")

if __name__ == '__main__':
    taskn()
