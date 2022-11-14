import main


def settings(lesson_number):
    manual = False
    test_count = 5
    print('Settings:')
    settings_list = {1: '1.. Manual - You would type all tests manually',
                     2: '2.. Auto - You would see generated results', }
    for number, variant in settings_list.items():
        print(variant)
    num = int(input('Please choose the manual type: '))
    print(f'You have been chosen: {settings_list[num]}')
    if num == 1:
        manual = True
    if num == 2:
        test_count = int(input('Please type the number of tests you wants to see: '))

    return main.start(lesson_number, manual, test_count)
