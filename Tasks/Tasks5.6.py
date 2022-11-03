def task_n(): #Here is main func for selecting which task you wants to check
    tasks = (Task1(), Task2(), Task3(), Task4(), Task5(), Task6()) #Here is variable which contains args which is our funcs of task
    tasks_count = len(tasks)
    print(f'For now, is ready for check {tasks_count} tasks'.center(50))
    while True:
        task_number = input('Please choose the number of task you are looking for:'.center(50))
        if task_number.isdigit(): #Check is inputed text is a number or not
            task_number = int(task_number)
            if task_number <= tasks_count:
                tasks[task_number - 1].start() #script to start our choosen task
            else:
                print('Choose the correct number'.center(50))
        elif task_number == 'esc': #extra func to exit the loop of choosing the tasks
            break
        else:
            print('Choose the correct number'.center(50))


class Task1:
    """
    Задание:
    "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.
    Вы должны написать программу, которая принимает положительное целое число и возвращает сл. значения.
    "Fizz Buzz", если число делится на 3 и 5;
    "Fizz", если число делится на 3;
    "Buzz", если число делится на 5;
    Число, как строку для остальных случаев.
    """
    def start(self):
        print('Task#1 [-Junior]')
        some_number = input('Please type the positive number: ')
        if some_number.isdigit():
            some_number = int(some_number)
            devision3 = some_number % 3
            devision5 = some_number % 5
            answer = ''
            if devision3 == 0:
                answer = answer + 'Fizz'
            if devision5 == 0:
                if answer == '':
                    answer = answer + 'Buzz'
                else:
                    answer = answer + ' Buzz'
            if answer == '':
                print(f'x = {some_number}, result: "{some_number}"')
            else:
                print(f'x = {some_number}, result: "{answer}"')
        else:
            print('Please type the correct number!')


class Task2:
    """
    Задание:
    Дано: Число x.
    Задание: нужно написать программу, которая дает оценку заданному значению, используя следующие правила.
    если x нечетное, то это "Плохо"
    если x = [2, 5] и четное, то это "Неплохо"
    если x = [6, 20] и четное, то это "Так себе"
    если x > 20 и четное, то это "Отлично"
    """
    def start(self):
        print('Task#2 [-Junior]')
        x = input('Please type any integer number: ')
        devision2 = int(x) % 2
        answer = ''
        if devision2 == 0:
            x = int(x)
            if x in range(2, 5):
                answer = 'Not Bad'
            if x in range(6, 20):
                answer = 'Weak'
            if x > 20:
                answer = 'Excellent'
        else:
            answer = 'Bad'
        print(f'x = {x}, result: "{answer}"')


class Task3:
    """
Дано: Число N = [1-9].
Задание: нужно написать программу, которая выведет последовательность 123..N
Пример:
 N = 3, результат: 123
 N = 9, результат: 123456789
 x = 1, результат: 1
    """
    def start(self):
        print('Task#3 [-Junior]')
        n = input('Please type the number between 1 and 9: ')
        answer = ''
        if n.isdigit():
            while int(n) > 0:
                answer = answer + str(n)
                n = int(n) - 1
            print(answer[::-1])
        else:
            print('Type the correct number')


class Task4:
    """
Дано: Дан кусок текста (str).
Задание: Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста. Подсказка: посмотрите внимательно на методы класса str.
Пример:
текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
    """
    def start(self):
        print('Task#4 [-Junior]')
        asker = input('Do you want to put your own text? [y/n]')
        if asker == 'n':
            print('We have some sort of text down here:')
            text = ('"Где умный человек прячет лист? В лесу. Но что если леса нет? ... Он выращивает лес и прячет его там." -- Гилберт Кит Честертон\n'
                  'Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты?\n'
                  'Вы можете использовать газету, чтобы рассказать кому-то свой секрет.\n'
                  'Даже если кто-то найдет ваше сообщение, легко отмахнуться и сказать что это паранойя и теория заговора.\n'
                  'Один из самых простых способов спрятать ваше секретное сообщение это использовать заглавные буквы.\n'
                  'Давайте найдем несколько таких секретных сообщений.\n')
            print(text)
        else:
            text = input('Type your text: ')
        input('Lets find out the uppercased string, please tap Enter to continue')
        i = 0
        answer = ''
        while i < len(text):
            testing = text[i]
            if ord(text[i]) in (range(ord('А'), ord('Я')+1)):
                answer += testing
            elif ord(text[i]) in (range(ord('A'), ord('Z')+1)):
                answer += testing
            i += 1
        print(answer)


class Task5:
    """
Дано: Строка со словами (str).
Задание: напишите программу, которая проверяет есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
Примеры:
text = "Hello World hello", результат: True
text = "He is 123 man", результат: False
text = "1 2 3 4", результат: False
    """
    def start(self):
        print('Task#5 [Junior]')
        text = input('Please type your text: ')
        text1 = text.split() #Here is we are splitting all our text string by string, it is sorting by blanks
        i = 0
        answer = 0
        final_answer = False
        while i < len(text1):
            if answer != 3: #Simple counter to find 3 words in a row
                    if text1[i].isdigit():
                        answer = 0
                    else:
                        answer += 1
            else:
                final_answer = True
            i += 1
        print(f'{text=}, result: {final_answer}')


class Task6:
    """
Дано: последовательность строк.
Задание: вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова.
Все строки даны в нижнем регистре.
Примеры:
["left", "right", "left", "stop"], результат: "left,left,left,stop"
["bright aright", "ok"], результат: "bleft aleft,ok"
["enough", "jokes"], результат: "enough,jokes"
    """
    def start(self):
        print('Task#6 [Junior+]')
        asker = input('Do you want to put your own text? [y/n]')
        if asker == 'n':
            print('We have some sort of text down here:')
            text = 'right alright,left stop,левши левшей,правши правшей'
            print(f'Here is a text for example of script work:\n{text}')
            input('Enter to see the result')
        else:
            text = input()
        rawtext = text.split(",") #Here is we are spliting our text by "," and making a list of them
        text = text.replace("right", "left")
        text = text.replace("правши", "левши")
        text = text.replace("правшей", "левшей")
        print(f'{rawtext}, result: {text}')


if __name__ == '__main__':
    task_n()
