def invert_personal_info(book: dict):
    """
    Дано: словарь ФИО - номер телефона(dict).
    Задание: получить новый словарь, инвертировав исходный, т.е. пары ключ - значение поменять местами (значение - ключ).
    Пример:
    book = {'Petr': '546810', 'Katya': '241815'}, результат: {'546810': 'Petr', '241815': 'Katya'}
    """
    default_book = {}
    for key, value in book.items():
        default_book.setdefault(value, key)
    return default_book


def invert_personal_info_view(book: dict):
    answer = invert_personal_info(book)
    return f'Referenced book: {book}\nInverted book: {answer}'


if __name__ == '__main__':
    book = {'Petr': '546810', 'Katya': '241815'}
    print(invert_personal_info_view(book))
