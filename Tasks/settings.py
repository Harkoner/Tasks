import main


class Settings:
    manual = False
    test_count = 8

    def main_settings(self):
        print('Settings:')
        settings_list = {1: '1.. Manual - You would type all tests manually',
                         2: '2.. Auto - You would see generated results', }
        for number, variant in settings_list.items():
            print(variant)
        num = int(input('Please choose the manual type: '))
        print(f'You have been chosen: {settings_list[num]}')
        if num == 1:
            Settings.manual = True
        if num == 2:
            Settings.manual = False
            Settings.test_count = int(input('Please type the number of tests you wants to see: '))
        return main.mainstart()
