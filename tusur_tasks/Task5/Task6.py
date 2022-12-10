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
    text = input()
    rawtext = ','.join(word for word in text)  #Here is we are spliting our text by "," and making a list of them
    rawtext = rawtext.replace("right", "left")
    rawtext = rawtext.replace("правши", "левши")
    rawtext = rawtext.replace("правшей", "левшей")
    return f'#{count} referenced: {text}, result: {rawtext}'