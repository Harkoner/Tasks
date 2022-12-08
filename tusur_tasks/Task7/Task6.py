import random


def cross_zero_play() -> list:
    data = ['X', 'O']
    game_result = []
    for x in range(3):
        game_result.append(random.choice(data) + random.choice(data) + random.choice(data))
    return game_result


def get_refery_decision(data: list) -> str:
    """
Дано: список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.
Задание.
Крестики-нолики - это игра для двух игроков (Х и О), которые расставляют эти знаки на 3х3 поле.
Игрок, который сумел разместить три своих знака в любой горизонтали, вертикали или диагонали -- выигрывает.
Но сейчас мы не будем играть в эту игру. Вы будете судить игру, и оценивать результат.
Вам дан результат игры, и вы должны решить, кто победил или что это ничья.
Ваша программа должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок.
В случае ничьи, результат должен быть "D".
Пример:
 data = [
    "X.O",
    "XX.",
    "XOO"
 ]  -> "X"
 data = [
    "OO.",
    "XOX",
    "XOX"
 ]  -> "O"
 data = [
    "OOX",
    "XXO",
    "OXX"
 ]  -> "D"
    """
    data_string = ''
    for string in data:
        data_string += string
    if data_string[1] == data_string[0] and data_string[2] == data_string[0]:
        return data_string[0]
    if data_string[3] == data_string[0] and data_string[6] == data_string[0]:
        return data_string[0]
    if data_string[4] == data_string[0] and data_string[8] == data_string[0]:
        return data_string[0]
    if data_string[4] == data_string[3] and data_string[5] == data_string[3]:
        return data_string[3]
    if data_string[7] == data_string[6] and data_string[8] == data_string[6]:
        return data_string[6]
    if data_string[4] == data_string[2] and data_string[6] == data_string[2]:
        return data_string[2]
    if data_string[4] == data_string[1] and data_string[7] == data_string[1]:
        return data_string[1]
    if data_string[5] == data_string[2] and data_string[8] == data_string[2]:
        return data_string[2]
    return 'D'


def get_refery_decision_view(data):
    answer = get_refery_decision(data)
    data_string = ''
    for string in data:
        data_string += f'{string}\n'
    if answer == 'D':
        return f'Result of the game:\n{data_string}Refery said that draw!'
    return f'Result of the game:\n{data_string}Refery said that {answer} won!'


if __name__ == '__main__':
    data = [
        "X.O",
        "XX.",
        "XOO"
    ]
    print(get_refery_decision_view(cross_zero_play()))
    # print(cross_zero_play())
