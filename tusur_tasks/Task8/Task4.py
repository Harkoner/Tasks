def decoder(data: tuple) -> str:
    """
    [Junior] 4. Дешифратор.
    Дано: шифровальная решетка (4 на 4) и зашифрованный пароль (4 на 4) представлены, как массив строк.
    Задание. Помогите Софи написать дешифратор для паролей, которые Никола зашифровал с помощью шифровальной решетки.
    Шифрорешетка - это квадрат 4 на 4 с четырьмя вырезанными окошками.
    Поместите решетку на листе бумаги такого же размера с буквами,
    выписываете первые 4 символа, которые видно в окошках (см. рисунок).
    Затем поверните решетку на 90 градусов по часовой стрелке.
    Выпишите следующие символы и повторите поворот. В итоге процедура повторяется 4 раза.
    Таким образом сложно узнать пароль без специальной решетки.
    Напишите программу, которая поможет проводить данную процедуру.
    Пример:
    (('X...',
    '..X.',
    'X..X',
    '....'),
    ('itdf',
    'gdce',
    'aton',
    'qrdi'), результат: 'icantforgetiddqd'

    (('....',
    'X..X',
    '.X..',
    '...X'),
    ('xhwc',
    'rsqx',
    'xqzz',
    'fyzr')), результат: 'rxqrwsfzxqxzhczy'
    """
    answer = ''
    crossed_list, pass_list = matrix_constructor(data)
    for _ in range(4):
        crossed_code = get_id(crossed_list)
        answer += get_decode(crossed_code, pass_list)
        crossed_list = rotator(crossed_list)
    return answer


def decoder_view(data: tuple) -> str:
    """
    Function as view for decoder
    """
    crossed_list, pass_list = matrix_constructor(data)
    answer = decoder(data)
    for i in range(4):
        print(f'{i + 1} iteration')
        for i in range(4):
            print(crossed_list[i], ' ', pass_list[i])
        crossed_code = get_id(crossed_list)
        print(f'decoder code: {crossed_code}')
        crossed_list = rotator(crossed_list)
        print('-' * 50)
    return f'Password: {answer}'


def get_id(crossed_list: list) -> list:
    """
    function making code as tuple from matrix of crossed list
    """
    crossed_code = []
    i = 0
    # Looking for indexes of X in crossed_list
    temp_crossed_list = crossed_list[:]
    for string in temp_crossed_list:
        for x in string:
            if x == 'X':
                crossed_code.append((i, string.index(x)))
                string[string.index(x)] = '1'
        i += 1
    # I don't know why it work differently than expected, so I have to move back "X"'s to crossed_list >_<
    for string in crossed_list:
        for x in string:
            if x == '1':
                string[string.index(x)] = 'X'
    return crossed_code


def get_decode(crossed_code, pass_list) -> str:
    """
    function decoding current matrix of crossed_code with original pass_list
    """
    answer = ''
    for i, j in crossed_code:
        answer += pass_list[i][j]
    return answer


def matrix_constructor(data: tuple) -> tuple:
    """
    matrix_contructor is function for making matrix of original data
    and returning tuple of 2 matrix as crossed_list pass_list
    """
    new_data = list(data)
    crossed_list = []
    pass_list = []
    tmp_list = []
    for string in new_data[0]:
        for element in string:
            tmp_list.append(element)
        crossed_list.append(tmp_list)
        tmp_list = []
    for string in new_data[1]:
        for element in string:
            tmp_list.append(element)
        pass_list.append(tmp_list)
        tmp_list = []
    return crossed_list, pass_list


def rotator(crossed: list) -> list:
    """
    function which rotating inputted matrix
    """
    length_string = len(crossed[0])
    rotated_crossed = []
    tmp_crossed = []
    for j in range(length_string):
        for i in range(length_string - 1, -1, -1):
            tmp_crossed.append(crossed[i][j])
        rotated_crossed.append(tmp_crossed)
        tmp_crossed = []
    return rotated_crossed


if __name__ == '__main__':
    data = (('X...',
             '..X.',
             'X..X',
             '....'),
            ('itdf',
             'gdce',
             'aton',
             'qrdi'))
    print(decoder_view(data))
