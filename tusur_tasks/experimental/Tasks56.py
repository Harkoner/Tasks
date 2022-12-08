import settings


def task1(count: int, some_number=123):

    """
    Задание:
    "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению.
    Давайте обучим компьютер.
    Вы должны написать программу, которая принимает положительное целое число и возвращает
    сл. значения.
    "Fizz Buzz", если число делится на 3 и 5;
    "Fizz", если число делится на 3;
    "Buzz", если число делится на 5;
    Число, как строку для остальных случаев.
    """
    if settings.Settings().manual:
        some_number = input('Please type the positive number: ')
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
        return f'#{count} x = {some_number}, result: "{some_number}"'
    else:
        return f'#{count} x = {some_number}, result: "{answer}"'


def task2(count: int, number=123):
    """
    Задание:
    Дано: Число x.
    Задание: нужно написать программу, которая дает оценку заданному значению, используя следующие правила.
    если x нечетное, то это "Плохо"
    если x = [2, 5] и четное, то это "Неплохо"
    если x = [6, 20] и четное, то это "Так себе"
    если x > 20 и четное, то это "Отлично"
    """
    if settings.Settings().manual:
        number = input('Please type any integer number: ')
    devision2 = int(number) % 2
    answer = ''
    if devision2 == 0:
        number = int(number)
        if number in range(2, 5):
            answer = 'Not Bad'
        if number in range(6, 20):
            answer = 'Weak'
        if number > 20:
            answer = 'Excellent'
    else:
        answer = 'Bad'
    return f'#{count} number = {number}, result: "{answer}"'


def task3(count: int, num=123):
    """
Дано: Число N = [1-9].
Задание: нужно написать программу, которая выведет последовательность 123..N
Пример:
 N = 3, результат: 123
 N = 9, результат: 123456789
 x = 1, результат: 1
    """
    if settings.Settings().manual:
        num = int(input('Please type the number between 1 and 9: '))
    number = num
    answer = ''
    while number > 0:
        answer = answer + str(number)
        number = number - 1
    return f'#{count} number = {num}, result: "{int(answer[::-1])}"'


def task4(count: int, text=''):
    """
Дано: Дан кусок текста (str).
Задание: Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
Подсказка: посмотрите внимательно на методы класса str.
Пример:
текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
    """
    if settings.Settings().manual:
        text = input('Type your text: ')
        # text = ('"Где умный человек прячет лист? В лесу. Но что если леса нет? ... '
        #         'Он выращивает лес и прячет его там." -- Гилберт Кит Честертон\n'
        #         'Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты?\n'
        #         'Вы можете использовать газету, чтобы рассказать кому-то свой секрет.\n'
        #         'Даже если кто-то найдет ваше сообщение, легко отмахнуться и сказать что это паранойя и теория заговора.\n'
        #         'Один из самых простых способов спрятать ваше секретное сообщение это использовать заглавные буквы.\n'
        #         'Давайте найдем несколько таких секретных сообщений.\n')
    i = 0
    answer = ''
    while i < len(text):
        testing = text[i]
        if ord(text[i]) in (range(ord('А'), ord('Я')+1)):
            answer += testing
        elif ord(text[i]) in (range(ord('A'), ord('Z')+1)):
            answer += testing
        i += 1
    return f'#{count} number = {text}, result: "{answer}"'


def task5(count: int, text= ''):
    """
Дано: Строка со словами (str).
Задание: напишите программу, которая проверяет есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
Примеры:
text = "Hello World hello", результат: True
text = "He is 123 man", результат: False
text = "1 2 3 4", результат: False
    """
    if settings.Settings().manual:
        text = input('Please type your text: ')
    text1 = text.split()  #Here is we are splitting all our text string by string, it is sorting by blanks
    i = 0
    answer = 0
    final_answer = False
    while i < len(text1):
        if answer != 3:  #Simple counter to find 3 words in a row
            if text1[i].isdigit():
                answer = 0
            else:
                answer += 1
        if answer == 3:
            final_answer = True
        i += 1
    return f'#{count} referenced: {text}, result: {final_answer}'


def task6(count: int, text):
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
    if settings.Settings().manual:
        # print('We have some sort of text down here:')
        # text = 'right alright,left stop,левши левшей,правши правшей'
        # print(f'Here is a text for example of script work:\n{text}')
        # input('Enter to see the result')
        text = input()
    rawtext = ','.join(word for word in text)  #Here is we are spliting our text by "," and making a list of them
    rawtext = rawtext.replace("right", "left")
    rawtext = rawtext.replace("правши", "левши")
    rawtext = rawtext.replace("правшей", "левшей")
    return f'#{count} referenced: {text}, result: {rawtext}'


if __name__ == '__main__':
    task_n()
