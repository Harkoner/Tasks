def task5(count: int, var=100500.345):
    """
    Дизайнер составил шаблон домашних ковриков. Для массового выпуска ковриков ему нужно уметь быстро составлять макет произвольного размера.
    Известно, что длина коврика всегда больше в 3 раза чем его ширина (W = 3 * H).
    Дано: ширина коврика.
    Задание: написать программу, которая будет составлять макет коврика для его дальнейшего производства.
    """

    def carpet(height_number):
        if height_number.isdigit():
            height = int(height_number)
            if height in range(10, 100, 1):
                width = height * 3
                print(f"Your carpet settings is {height:} and {width:}\n")
                print('Lets make them!'.center(width))
                for stick_count in range(1, height, 2):
                    print(('.|.' * stick_count).center(width, '-'))
                print('Presented by Nikolay Kriger'.center(width, '-'))
                for stick_count in range(height - 2, 0, -2):
                    print(('.|.' * stick_count).center(width, '-'))
            elif height not in range(10, 100, 1):
                print('Choose the correct number'.center(50))
                return task5(count)
        else:
            print('Please use only numbers between 10 and 99!'.center(50))
            return task5(count)
        return 'Thank you for using our service!'
    var = input("Please enter the height between 10 and 99: ")
    return carpet(var)
