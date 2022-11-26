import random
from random import randint
import settings


def task1(count, text='Hello world of the world'):
    """
    Дано: текст (str).
    Задание: необходимо получить 2 словаря (популярности слов и популярности букв).
    Пример:
    text = "hello, word of word", результат:
    chars_popularity = {'h': 1, 'e': 1, 'l': 2, ..};
    words_popularity = {'hello': 1, 'word': 2, 'of': 1}
    """

    words_popularity_list = text.split()
    chars_popularity = {}
    words_popularity = {}
    for liter in set(text):
        if liter.isalpha():
            chars_popularity.setdefault(liter, text.count(liter))
    for word in words_popularity_list:
        words_popularity.setdefault(word, text.count(word))
    return f'{chars_popularity}\n{words_popularity}'


def task2(count, ciphra: int):
    """
    Дано: целое число (int).
    Задание: Римские цифры пришли к нам из древней римской системы счета.
    Они основаны на особых буквах алфавита, которые в различных сочетаниях,
    путем суммирования (а иногда и разницы) описывают различные числа.
    Первые 10 римских чисел это:
    I, II, III, IV, V, VI, VII, VIII, IX, and X.
    Римская система счета имеет десятичное основание, но она непозиционная и не включает в себя 0 (ноль).
    Римские числа образуются путем комбинации следующих семи символов:
    Символ Значение
    I 1 (unus) V 5 (quinque) X 10 (decem) L 50 (quinquaginta) C 100 (centum) D 500 (quingenti) M 1,000 (mille)
    В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999) в римскую систему счета.
    Пример:
    x = 6, результат: 'VI'
    x = 76, результат: 'LXXVI'
    x = 13 , результат: 'XIII'
    x = 44 , результат: 'XLIV'
    x = 3999 , результат: 'MMMCMXCIX'
    """
    rim_dict = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I',
    }
    number = ciphra
    answer = ''
    while number > 0:
        if number == 9:
            answer += 'IX'
            number -= 9
        if number == 8:
            answer += 'VIII'
            number -= 8
        if number == 7:
            answer += 'VII'
            number -= 7
        if number == 6:
            answer += 'VI'
            number -= 6
        if number == 4:
            answer += 'IV'
            number -= 4
        for num, liter in rim_dict.items():
            if number >= num:
                answer += liter
                number -= num
                break
    # Another attempt
    # while number > 0:
    #     if number == 9:
    #         answer += 'IX'
    #         number -= 9
    #     if number == 6:
    #         answer += 'VI'
    #         number -= 6
    #     if number == 4:
    #         answer += 'IV'
    #         number -= 4
    #     if number >= 1000:
    #         answer += 'M'
    #         number -= 1000
    #         continue
    #     if number >= 500:
    #         answer += 'D'
    #         number -= 500
    #         continue
    #     if number >= 100:
    #         answer += 'C'
    #         number -= 100
    #         continue
    #     if number >= 50:
    #         answer += 'L'
    #         number -= 50
    #         continue
    #     if number >= 10:
    #         answer += 'X'
    #         number -= 10
    #         continue
    #     if number >= 5:
    #         answer += 'V'
    #         number -= 5
    #         continue
    #     if number == 1:
    #         answer += 'I'
    #         number -= 1
    # for num in str(number):
    #     num = int(num)
    #     if num > 1000:
    #
    return answer, ciphra


# бизнес логика
def task3():
    """
Дано: словарь банк - курс доллара (dict).
Задание: определить банк и курс покупки валюты с наиболее привлекательным предложением.
Пример:
rates = {'Sberbank': 55.8, 'VTB24': 53.91}, результат: VTB24 -> 53.91
    """

    def random_value():
        return '{:.2f}'.format(random.uniform(50.0, 60.0))

    rates = {
        'Sberbank': random_value(),
        'VTB24': random_value(),
        'VTB34': random_value(),
        'Kaspi': random_value(),
        'OldBank': random_value(),
    }
    bank_title = list(rates.keys())
    bank_value = list(rates.values())
    min_bank_value = min(bank_value)
    min_bank_title = bank_title[(bank_value.index(min_bank_value))]

    return [rates, min_bank_title, min_bank_value]


# представление
def task3_view():
    got = task3()
    return f'{got[1]} -> {got[2]}'


if __name__ == '__main__':
    print(task3())
    print(task3_view())
    # print(Task2(1, randint(1, 3999)))
