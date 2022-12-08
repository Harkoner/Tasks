def popularity(text: str) -> list:
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
    return [chars_popularity, words_popularity]


# представление
def popularity_view(text):
    view = popularity(text)
    return f'Original text = \"{text}\"\nchars_popularity = {view[0]}\nwords_popularity = {view[1]}'


if __name__ == '__main__':
    user_text = input('Type a text or just Enter to see result\n')
    if user_text == '':
        text = 'Hello world of the world'
    else:
        text = user_text
    print(popularity_view(text))
