#Task1
print('Task#1')
print('Welcome to the python\n'
      'Lets get started!\n'
      'Please enter your First name\n')
firstname = input()
print('What is your last name?')
secondname = input()
print(f"Hello, {firstname.title()} {secondname.title()}!, you just delved into Python. Great start")


#Task2
print('Task#2')
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
"""Так как у нас уже есть текст с первой задачи, используем его и выведем Фамилию и имя большими буквами"""
print('Task#3')
print('Hello', firstname.title(), secondname.title()+'!', 'You just delved into Python. Great start!')

#Task4
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