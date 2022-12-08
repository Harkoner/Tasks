from random import randint

def get_roman_numbers(ciphra: int) -> str:
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
    return answer


def get_roman_numbers_view(ciphra: int):
    answer = get_roman_numbers(ciphra)
    return f'x = {ciphra}, result: {answer}'


if __name__ == '__main__':
    user_ciphra = input('Type a number or just Enter to see result\n')
    if user_ciphra == '':
        ciphra = randint(1, 3999)
    else:
        ciphra = int(user_ciphra)
    print(get_roman_numbers_view(ciphra))
