def task_n():
    tasks = (Task1(), Task2(), Task3(), Task4())
    print('For now, is ready for check 5 tasks'.center(50))
    while True:
        task_number = input('Please choose the number of task you are looking for:'.center(50))
        if task_number.isdigit():
            task_number = int(task_number)
            if task_number <= 4:
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


if __name__ == '__main__':
    task_n()
