import Tests
import settings
import requests
import itertools


# Module pickle

class WordsAsker:
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    lessons = {
        1: 'Tasks36.py',
        2: 'Tasks46.py',
        3: 'Tasks56.py',
        4: 'Tasks67.py',
        5: 'Tasks7.py',
        6: 'Settings',
        7: 'Exit the program',
    }
    iteration = False
    # def get_on_top(self, lesson):
    #     return WordsAsker.lessons[lesson]


# Декоратор для страницы с заданиями
def monitor(func):
    right = 25

    # ╠ ═ ╣ ╔ ╦ ╗ ║ ╚ ╩ ╝ ╬ ═
    def realiser(*args, **kwargs):
        terra = func(*args, **kwargs)
        # on_top = WordsAsker.get_on_top(*args, **kwargs)
        on_top = 1
        for index in args:
            on_top = WordsAsker.lessons[index]
        centralise = int(
            ((len('║'.ljust(1)) + len(on_top) + len('║'.rjust(right - 1 - len(on_top), ' '))) / 2) - (len(on_top)) / 2)
        print('╔'.ljust(right + 1, '═') + '╗')
        print('║'.ljust(1), ' ' * (centralise - 1), on_top, '║'.rjust(right - 1 - len(on_top) - centralise, ' '))
        print('╠'.ljust(right + 1, '═') + '╣')
        for line in terra:
            print('║'.ljust(1), line, '║'.rjust(right - 1 - len(line), ' '))
        print('╚'.ljust(right + 1, '═') + '╝')

    return realiser


# Декоратор для главной страницы
def main_monitor(func):
    right = 25

    # ╠ ═ ╣ ╔ ╦ ╗ ║ ╚ ╩ ╝ ╬ ═
    def realiser(*args, **kwargs):
        terra = func(*args, **kwargs)
        on_top = 'Main board'
        centralise = int(((len('║'.ljust(1)) + len(on_top) + len('║'.rjust(right - 1 - len(on_top), ' '))) / 2) - (
            len(on_top)) / 2)
        print('╔'.ljust(right + 1, '═') + '╗')
        print('║'.ljust(1), ' ' * (centralise - 1), on_top, '║'.rjust(right - 1 - len(on_top) - centralise, ' '))
        print('╠'.ljust(right + 1, '═') + '╣')
        for line in terra:
            print('║'.ljust(1), line, '║'.rjust(right - 1 - len(line), ' '))
        print('╚'.ljust(right + 1, '═') + '╝')

    return realiser


# Декоратор для вывода только тестов
def tests_monitor(func):
    right = 70

    # ╠ ═ ╣ ╔ ╦ ╗ ║ ╚ ╩ ╝ ╬ ═
    def realiser(*args, **kwargs):
        terra = func(*args, **kwargs)
        # on_top = WordsAsker.get_on_top(*args, **kwargs)
        on_top = 'Tests'
        centralise = int(((len('║'.ljust(1)) + len(on_top) + len('║'.rjust(right - 1 - len(on_top), ' '))) / 2) - (
            len(on_top)) / 2)
        print('╔'.ljust(right + 1, '═') + '╗')
        print('║'.ljust(1), ' ' * (centralise - 1), on_top, '║'.rjust(right - 1 - len(on_top) - centralise, ' '))
        print('╠'.ljust(right + 1, '═') + '╣')
        for line in terra:
            print('║'.ljust(1), line, '║'.rjust(right - 1 - len(line), ' '))
        print('╚'.ljust(right + 1, '═') + '╝')

    return realiser


# Декоратор для вывода меню и тестов одновременно
def monitor_lessons_tests(func):
    right = 25
    rright = 90

    # ╠ ═ ╣ ╔ ╦ ╗ ║ ╚ ╩ ╝ ╬ ═
    def realiser(*args, **kwargs):
        terra = func(*args, **kwargs)
        x, y = args[0], args[1]
        on_top = WordsAsker.lessons[x]
        centralise = int(
            ((len('║'.ljust(1)) + len(on_top) + len('║'.rjust(right - 1 - len(on_top), ' '))) / 2) - (len(on_top)) / 2)

        print('╔'.ljust(right + 1, '═') + '╦' + ''.rjust(rright - 1, '═') + '╗')
        print('║'.ljust(1), ' ' * (centralise - 1), on_top, '║'.rjust(right - 1 - len(on_top) - centralise, ' ') +
              ''.rjust(int((rright - 1) / 2) - 2, ' ') + 'Tests' + ''.rjust(int((rright - 1) / 2) - 2, ' ') + '║')
        print('╠'.ljust(right + 1, '═') + '╬' + ''.rjust(rright - 1, '═') + '╣')

        first_terra = terra[0]
        second_terra = terra[1]
        ara = itertools.zip_longest(first_terra, second_terra)
        for line, test in ara:
            test = test if test else ' '
            line = line if line else ' '
            print('║'.ljust(1), line, '║'.rjust(right - 1 - len(line), ' '), test, '║'.rjust(rright - 2 - len(test), ' '))
        print('╚'.ljust(right + 1, '═') + '╩' + ''.rjust(rright - 1, '═') + '╝')

    return realiser


def mainstart():
    current_main_board()
    lesson_number = int(input('please select the point by typing his number: '))
    if lesson_number == len(WordsAsker.lessons) - 1:
        return settings.Settings().main_settings()
    if lesson_number == len(WordsAsker.lessons):
        return print('Thank you for using our program!'.center(50))
    WordsAsker.iteration = False
    start(lesson_number)
    mainstart()


def dict_task_lists(lesson_number=None):
    tasks_list = {
        1: {1: 'Task#1 - [-Junior]',
            2: 'Task#2 - [-Junior]',
            3: 'Task#3 - [-Junior]',
            4: 'Task#4 - [-Junior]',
            5: 'Task#5 - [Junior]',
            6: 'Task#6 - [+Junior]',
            7: 'Settings',
            8: 'Back to main', },
        2: {1: 'Task#1 - [-Junior]',
            2: 'Task#2 - [-Junior]',
            3: 'Task#3 - [-Junior]',
            4: 'Task#4 - [Junior]',
            5: 'Task#5 - [+Junior]',
            6: 'Settings',
            7: 'Back to main', },
        3: {1: 'Task#1 - [-Junior]',
            2: 'Task#2 - [-Junior]',
            3: 'Task#3 - [-Junior]',
            4: 'Task#4 - [-Junior]',
            5: 'Task#5 - [Junior]',
            6: 'Task#6 - [+Junior]',
            7: 'Settings',
            8: 'Back to main', },
        4: {1: 'Task#1 - [-Junior]',
            2: 'Task#2 - [-Junior]',
            3: 'Task#3 - [-Junior]',
            4: 'Task#4 - [Junior]',
            5: 'Task#5 - [+Junior]',
            6: 'Settings',
            7: 'Back to main', },
        5: {1: 'Task#1 - [-Junior]',
            # 2: 'Task#2 - [-Junior]',
            # 3: 'Task#3 - [-Junior]',
            # 4: 'Task#4 - [Junior]',
            # 5: 'Task#5 - [+Junior]',
            6: 'Settings',
            7: 'Back to main', },
    }
    if lesson_number is None:
        return mainstart()
    return tasks_list[lesson_number]


def start(lesson_number: int):
    counter = 1
    tests = []
    calldict = dict_task_lists(lesson_number)
    if not WordsAsker.iteration:
        current_lesson_and_tests(lesson_number, tests)
    num = int(input('please select the point by typing his number: '))
    if num == len(calldict) - 1:
        return settings.Settings().main_settings()
    if num != len(calldict):
        num = int(num)
        # print(calldict[num])
        if settings.Settings().manual:
            # print(Tests.tests(num, counter, lesson_number))
            tests.append(Tests.tests(num, counter, lesson_number))
        else:
            while counter < settings.Settings().test_count + 1:
                tests.append(Tests.tests(num, counter, lesson_number))
                counter += 1
        WordsAsker.iteration = True
        current_lesson_and_tests(lesson_number, tests)
        start(lesson_number)


@monitor
def current_lesson(lesson):
    n = 1
    answer = []
    for number, variant in dict_task_lists(lesson).items():
        answer.append(f'{n}.. ' + variant)
        n += 1
    return answer


@monitor_lessons_tests
def current_lesson_and_tests(lesson, test):
    n = 1
    lesson_answer = []
    for number, variant in dict_task_lists(lesson).items():
        lesson_answer.append(f'{n}.. ' + variant)
        n += 1
    answer = [lesson_answer, test]

    return answer


@main_monitor
def current_main_board():
    n = 1
    answer = []
    for number, variant in WordsAsker.lessons.items():
        answer.append(f'{n}.. ' + variant)
        n += 1
    return answer


@tests_monitor
def show_test(tests):
    return tests


if __name__ == '__main__':
    mainstart()
