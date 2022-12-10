def task5(count: int, text= ''):
    """
Дано: Строка со словами (str).
Задание: напишите программу, которая проверяет есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
Примеры:
text = "Hello World hello", результат: True
text = "He is 123 man", результат: False
text = "1 2 3 4", результат: False
    """
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
