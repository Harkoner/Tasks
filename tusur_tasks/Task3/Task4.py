def task4(count: int, var=100500.345):
    """
    Дано: денежная сумма (amount > 0).
    Задание: написать программу, которая распечатает число в принятом денежном формате XXX,XXX.XX.
    Пример: amount = 100500.157; результат = 100,500.16
    """
    # var = float(input('Type the float number: '))
    return f"#{count} Number: {var}, Result: {'{0:3,.3f}'.format(var)}"