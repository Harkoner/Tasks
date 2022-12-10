def task3(count: int, number=123.123):
    """
    Дано: число с плавающей точкой.
    Задание: написать программу, которая будет округлять заданное число:
    2-х знаков после запятой;
    до целого;
    дополнять слева столько нулей, сколько не хватает числу до 11 знаков.
    Пример:
    x = 14.721
    14.72
    15
    0000014.721
    """
    number = float(input('Please type the float number: '))
    float_number = '{:.2f}'.format(number)
    int_number = int(number + (0.5 if (number - int(number)) > 0.5 else 0))
    number = '{:.3f}'.format(number)
    null_float_number = '{:=011}'.format(float(number))
    return f'#{count} Referece: {number}, 1) {float_number}, 2) {int_number}, 3) {null_float_number}'