

def check_parenthesis(p_string: str) -> bool:

    '''

    Проверка правильности постановки скобок в строке.

    :param p_string: строка, в которой будем проверять правильность постановки скобок.

    :return: Возвращает True или False как ответ на вопрос правильно ли поставлены скобки в строке.


    '''

    if p_string == '':

        return True

    for pair in ('()', '{}', '[]'):

        if pair in p_string:

            return check_parenthesis(p_string.replace(pair, '', 1))

    return False


String = input('Enter a string: ')
P_string =  ''.join[ch for ch in String if ch in '(){}[]']
result = check_parenthesis(P_string)

print(result)
