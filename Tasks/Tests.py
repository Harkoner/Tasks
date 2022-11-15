import main
import Tasks36
import Tasks67
from random import uniform
from random import randint
import random


def tests(num_task: int,
          count: int,
          manual: bool,
          file_name: int) -> 'Call a func: tasks[num_task](test object, count)':
    word_list = main.WordsAssker.WORDS
    tasks = {
        1: {1: Tasks36.task1,
            2: Tasks36.task2,
            3: Tasks36.task3,
            4: Tasks36.task4,
            5: Tasks36.task5,
            6: Tasks36.task6,
            },
        4: {
            1: Tasks67.task1,
            2: Tasks67.task2,
            3: Tasks67.task3,
            4: Tasks67.task4,
            5: Tasks67.task5,
        }
    }

    first_name = ['kolya', 'igor', 'vasya', 'anatoliy', 'sasha', 'tanya', 'ivan', 'stepa', 'nastya', 'vitaly']
    last_name = ['Levine', 'Raven', 'Hansley', 'West', 'Marley', 'Lopez', 'Cassidy', 'Poverly', 'Beckett', 'Pierce']

    tests = {
        1: {1: f'{random.choice(first_name)} {random.choice(last_name)}',
            2: 'not needed',
            3: 'not needed',
            4: uniform(100_000, 100_500),
            5: str(randint(10, 100)),
            6: randint(1, 10000),
            },
        4: {
            1: [randint(0, 20) for i in range(randint(0, 8))],
            2: [random.uniform(-5.0, 15.0) for i in range(randint(0, 8))],
            3: [randint(-20, 70) for i in range(5)],
            4: [randint(0, 200) for i in range(randint(1, 7))],
            5: ''.join([str(random.choice(word_list))[2:-1] + ' ' for x in range(randint(3, 7))])[
               :-1] if num_task == 5 else '',
        }
    }
    if manual == True:
        return tasks[file_name][num_task](count, manual)
    else:
        return tasks[file_name][num_task](count, manual, tests[file_name][num_task])