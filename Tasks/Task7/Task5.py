def collect_dict(dates: list, rates: list) -> dict:
    """
Дано: 2 списка с измерениями(list).
Задание. Ученый-спекулянт анализировал курс доллара и собрал 2 списка: один с датами (dates),
а другой с курсами валют (rates).
Он знает, что эти списки имеют одинаковую длину,
а также что i-ый курс из списка rates соотвествует i-ой дате из списка dates.
Друзья ученого, зная о его исследовании, часто просят его предоставить значение курса валюты на определенную дату.
Так как ученый-спекулянт изучает Python, то решил составить словарь, что позволит ему быстро получать такую информацию.
Формально нужно получить словарь из 2-х списков, где в первом находятся ключи, а во втором значения.
Пример:
dates = ['2017-03-01', '2017-03-02'], rates = [55.7, 55.2], результат:
{'2017-03-01': 55.7, '2017-03-02': '55.2}
    """
    answer = {dates[i]: rates[i] for i in range(len(dates))}
    return answer


def collect_dict_view(dates: list, rates: list) -> str:
    """
    :param dates: Shows the dates of test
    :param rates: Shows the rates of test
    :return: view of dates + rates as dict
    """
    answer = collect_dict(dates, rates)
    return f'Referenced dates: {dates}\nReferenced rates: {rates}\nCollected dictionary: {answer}'


if __name__ == '__main__':
    dates = ['2017-03-01', '2017-03-02']
    rates = [55.7, 55.2]
    print(collect_dict_view(dates, rates))
