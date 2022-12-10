def task5(count: int,
          text=''):
    """
    Дано: текст, как строка (str).
    Задание: Наши Роботы никогда не упускают возможности, чтобы улучшить свои навыки в лингвистике. Сейчас они изучают английский алфавит и что с этим делать.
    Алфавит разделен на гласные и согласные буквы (да, мы разделили буквы, а не звуки).
    Гласные -- A E I O U Y
    Согласные -- B C D F G H J K L M N P Q R S T V W X Z
    Дан текст с разными словами и/или числами, которые разделены пробелами и знаками пунктуации.
    Числа не считаются за слова (также как и смесь букв и цифр).
    Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными (полосатые слова),
    то есть в таких словах нет двух гласных или двух согласных букв подряд.
    Слова состоящие из одной буквы - не "полосатые" (не считайте их).
    Регистр букв не имеет значения.
    Пример:
    text = "My name is ...", результат: 3
    text = "Hello world", результат: 0
    text = "A quantity of striped words.", результат: 1
    text = "Dog,cat,mouse,bird.Human.", результат: 3
    """
    text = (input('please type the numbers in format "Hello world. Hows your day today?": '))
    vowels = 'aAeEiIoOuUyY'
    consonant = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZ'
    i = 0  # num of liter
    answer = 0
    final_answer = 0
    text_list = text.split()
    for words in text_list:
        if len(words) != 1:
            while i + 1 < len(words):
                if words[i] in vowels and words[i + 1] in vowels:
                    answer += 1
                elif words[i] in consonant and words[i + 1] in consonant:
                    answer += 1
                i += 1
            i = 0
            if answer == 0:
                final_answer += 1
            answer = 0
    return f'#{count} referenced: "{text}" result: {final_answer}'
