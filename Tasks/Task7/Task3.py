import random


def get_better_bank():
    """
Дано: словарь банк - курс доллара (dict).
Задание: определить банк и курс покупки валюты с наиболее привлекательным предложением.
Пример:
rates = {'Sberbank': 55.8, 'VTB24': 53.91}, результат: VTB24 -> 53.91
    """

    def random_value():
        return '{:.2f}'.format(random.uniform(50.0, 60.0))

    rates = {
        'Sberbank': random_value(),
        'VTB24': random_value(),
        'VTB34': random_value(),
        'Kaspi': random_value(),
        'OldBank': random_value(),
    }
    bank_title = list(rates.keys())
    bank_value = list(rates.values())
    min_bank_value = min(bank_value)
    min_bank_title = bank_title[(bank_value.index(min_bank_value))]

    return [rates, min_bank_title, min_bank_value]


# представление
def get_better_bank_view():
    got = get_better_bank()
    bank_list = ''
    for bank, value in got[0].items():
        bank_list += f'{bank}: {value}\n'
    return f'Current bank rates:\n{bank_list}\nBest choise is:\n{got[1]} -> {got[2]}'


if __name__ == '__main__':
    print(get_better_bank_view())
