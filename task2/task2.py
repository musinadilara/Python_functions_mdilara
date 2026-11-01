def fibonacci_seq(n: int) -> int:

    '''

       Поиск запрошенного элемента ряда Фибоначчи.

       :param n: номер запрошенного элемента ряда Фибоначчи.

       :return: Возвращает запрошенный элемент ряда Фибоначчи.

    '''

    if n == 0:

        return 0

    elif n == 1:

        return 1

    else:

        return fibonacci_seq(n - 1) + fibonacci_seq(n - 2)


N = int(input('Enter an integer: '))
result = fibonacci_seq(N)

print(result)