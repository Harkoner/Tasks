import Tests
import settings
import requests


def mainstart(manual=False, test_count=5):
    lessons = {
        1: '1st lesson tasks (Tasks36.py)',
        # 2: '2nd lesson tasks (Tasks46.py)',
        # 3: '3rd lesson tasks (Tasks56.py)',
        4: '4th lesson tasks (Tasks67.py)',
        # 5: '5th lesson tasks (Tasks36.py)',
    }
    n = 1
    for number, variant in lessons.items():
        print(f'{n}.. ' + variant)
        n += 1
    lesson_number = int(input('please select the point by typing his number: '))
    if lesson_number == 6:
        return print('Thank you for using our program!'.center(50))
    start(lesson_number, manual, test_count)
    mainstart()


def dict_task_lists(lesson_number):
    tasks_list = {
        1: {1: 'Task#1 - [-Junior]',
            2: 'Task#2 - [-Junior]',
            3: 'Task#3 - [-Junior]',
            4: 'Task#4 - [-Junior]',
            5: 'Task#5 - [Junior]',
            6: 'Task#6 - [+Junior]',
            7: 'Settings',
            8: 'Exit the program', },
        4: {1: 'Task#1 - [-Junior]',
            2: 'Task#2 - [-Junior]',
            3: 'Task#3 - [-Junior]',
            4: 'Task#4 - [Junior]',
            5: 'Task#5 - [+Junior]',
            6: 'Settings',
            7: 'Exit the program', },
    }
    return tasks_list[lesson_number]


def start(lesson_number=1, manual=False, test_count=5):
    counter = 1
    n = 1
    calldict = dict_task_lists(lesson_number)
    for number, variant in dict_task_lists(lesson_number).items():
        print(f'{n}.. ' + variant)
        n += 1
    num = int(input('please select the point by typing his number: '))
    if num == len(calldict)-1:
        return settings.settings(lesson_number)
    if num != len(calldict):
        num = int(num)
        print(calldict[lesson_number])
        if manual == False:
            while counter < test_count + 1:
                print(Tests.tests(num, counter, manual, lesson_number))
                counter += 1
        else:
            print(Tests.tests(num, counter, manual, lesson_number))
        input('Enter to continue')
        start(lesson_number, manual, test_count)


class WordsAssker:
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()


if __name__ == '__main__':
    mainstart()