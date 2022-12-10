"""
    Дано: слово, состоящее только из строчных латинских букв.
    Задание: написать функцию, которая возвращает True, если слово палиндромом, иначе False.
    Палиндро́м — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях.
    Например, число 404; слова «топот» в русском языке; текст «а роза упала на лапу Азора» и пр.
    Примеры:
    'lol', результат: True
    'hi', результат: False
"""


def get_palindrome(data):
    answer = True
    flip_list = []
    flip_data = ''
    for x in data:
        flip_list.append(x)
    for x in flip_list[::-1]:
        flip_data += x
    for i in range(len(data)):
        if data[i] != flip_data[i]:
            answer = False
    return answer


def get_palindrome_view(data):
    answer = get_palindrome(data)
    return f'{data}, result: {answer}'


if __name__ == '__main__':
    data = 'lol'
    print(get_palindrome_view(data))
