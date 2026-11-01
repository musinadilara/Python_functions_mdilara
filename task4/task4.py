
def factorial(num: int) -> int:

    '''

    Поиск факториала числа.

    :param num: число, факториал которого мы ищем.

    :return: Возвращает найденный факториал числа.

    '''

    if num == 0:

        return 1

    else:

        return num * factorial(num - 1)


N = int(input('Введите натуральное число n: '))

print('Факториалы от 1 до n:')


for i in range(1, N + 1):

    print(i, factorial(i))


