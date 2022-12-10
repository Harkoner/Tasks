"""
Дано: степень прозрачности, как целое число.
Задание. У Николы появилось свободное время и он решил заняться исследованием привидений.
Он хочет найти способ, как определять возраст привидений.
Согласно древним фолиантам, возраст связан со степенью прозрачности призраков.
Никола составил шкалу измерений прозрачности
от 10000 до 0, где 10000 - это совсем не прозрачное "новорождённое" привидение
(0 лет) и 0 - это уже невидимка (возраст неизвестен).
После множества экспериментов, Никола кажется начел взаимосвязь.
На каждый "день рождения", степень прозрачности привидения уменьшается на количество единиц,
равное его возрасту, если возраст есть одно из чисел Фибоначчи (подробней здесь),
иначе увеличивается на единицу.
Для примера: "Новорождённое" привидение -- 10000 единиц прозрачности.
1 год -- 10000 - 1 = 9999 (1 число Фибоначчи).
2 года -- 9999 - 2 = 9997 (2 число Фибоначчи).
3 года -- 9997 - 3 = 9994 (3 число Фибоначчи).
4 года -- 9994 + 1 = 9995 (4 не число Фибоначчи).
5 лет -- 9995 - 5 = 9990 (5 число Фибоначчи).
Помогите Николе написать функцию, которая будет определять возраст привидения по прозрачности.
Вам известно измерение прозрачности, как число от 0 до 10000 включительно.
Привидения не бывают старше 5000 лет, так как потом просто исчезают (серьезно, научный факт).
Пример:
прозрачность = 10000, возраст: 0
прозрачность = 9999, возраст: 1
прозрачность = 9997, возраст: 2
прозрачность = 9994, возраст: 3
прозрачность = 9995, возраст: 4
прозрачность = 9990, возраст: 5
"""
from random import randint


def get_age_of_casper(transparency: int) -> int:
    """
    function which calc the age of casper
    and return his age as int
    """
    fibonacci = get_fibonacci_10000()
    age = 0
    almost_transparency = 10000
    while True:
        if age in fibonacci:
            almost_transparency -= age
        else:
            almost_transparency += 1
        if transparency == almost_transparency:
            break
        age += 1
    return age


def get_fibonacci_10000() -> list:
    """
    function to get fibonacci numbers up to 10000 as list
    """
    fibonacci = [0, 1, 1]
    while True:
        if fibonacci[-2] + fibonacci[-1] > 10000:
            break
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci


def get_age_of_casper_view(transparency: int) -> str:
    """
    function as view for function get_age_of_casper
    """
    age = get_age_of_casper(transparency)
    casper_class = 'Realable casper'
    if age > 5000:
        casper_class = 'Unreal casper (too old)'
    return f'transparency = {transparency}, age = {age}, class = {casper_class}'


if __name__ == '__main__':
    print(get_age_of_casper_view(randint(1, 10000)))
