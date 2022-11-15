import Tests
import settings
import requests


def mainstart():
    print('Main board')
    lessons = {
        1: '1st lesson tasks (Tasks36.py)',
        2: '2nd lesson tasks (Tasks46.py)',
        3: '3rd lesson tasks (Tasks56.py)',
        4: '4th lesson tasks (Tasks67.py)',
        5: 'Settings',
        6: 'Exit the program',
        # 7: '5th lesson tasks (Tasks36.py)',
    }
    n = 1
    for number, variant in lessons.items():
        print(f'{n}.. ' + variant)
        n += 1
    lesson_number = int(input('please select the point by typing his number: '))
    if lesson_number == len(lessons) - 1:
        return settings.Settings().main_settings()
    if lesson_number == len(lessons):
        return print('Thank you for using our program!'.center(50))
    start(lesson_number)
    mainstart()


def dict_task_lists(lesson_number=999):
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
    }
    if lesson_number == 999:
        return mainstart()
    return tasks_list[lesson_number]


def start(lesson_number):
    counter = 1
    n = 1
    calldict = dict_task_lists(lesson_number)
    for number, variant in dict_task_lists(lesson_number).items():
        print(f'{n}.. ' + variant)
        n += 1
    num = int(input('please select the point by typing his number: '))
    if num == len(calldict) - 1:
        return settings.Settings().main_settings()
    if num != len(calldict):
        num = int(num)
        print(calldict[num])
        if settings.Settings().manual:
            print(Tests.tests(num, counter, lesson_number))
        else:
            while counter < settings.Settings().test_count + 1:
                print(Tests.tests(num, counter, lesson_number))
                counter += 1
        input('Enter to continue')
        start(lesson_number)


class WordsAssker:
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()


if __name__ == '__main__':
    mainstart()
