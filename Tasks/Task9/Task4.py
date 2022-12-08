import random


# main
def get_safe_pawns(data: set) -> tuple:
    num_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
    }
    game_field = []
    new_data = []
    answer = 0
    field_size = 10
    # making game field
    for raw in range(field_size):
        game_field.append(['.'] * field_size)
    # Transforming incoming data to new type of data
    for value in data:
        new_data.append(value[1] + str(num_dict[value[0]]))
    # filling our game field with our pawns
    for value in new_data:
        game_field[int(value[0])][int(value[1])] = '1'
    # Checking guard status
    for value in new_data:
        val0 = int(value[0])
        val1 = int(value[1])
        if game_field[val0 - 1][val1 - 1] == '1':
            answer += 1
        elif game_field[val0 - 1][val1 + 1] == '1':
            answer += 1
    return answer, game_field[::-1]


# view
def get_safe_pawns_view(data: set) -> str:
    answer, game_field = get_safe_pawns(data)
    print('Game Field')
    for raw in game_field[1:-1]:
        print(f'{raw[1:-1]}')
    return f'The number of safe pawns is {answer}'


# function to make a random positions of pawns for test
def pawns_position() -> set:
    data = []
    liters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    while len(set(data)) != 8:
        data.append(random.choice(liters) + random.choice(numbers))
    return set(data)


if __name__ == '__main__':
    data = pawns_position()
    print(get_safe_pawns_view(data))
