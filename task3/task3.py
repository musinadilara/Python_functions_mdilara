import re


def find_abbreviations(string: str) -> str:

      '''

         Поиск аббревиатур в строке с помощью регулярных выражений.

         :param string: строка, в которой происходит поиск аббревиатур.

         :return: Возвращает все найденные аббревиатуры через запятую единой строкой.

      '''

      abbreviations = re.findall(r'\b[A-ZА-Я]{1,6}\b', String)
      result = ', '.join(abbreviations)

      return result


String = str(input('Enter a string: '))
result = find_abbreviations(String)

print(f'Abbreviations found: {result}.')


#МГУ, МГТУ - это вузы РФ. ИТИС - это лучший институт КФУ