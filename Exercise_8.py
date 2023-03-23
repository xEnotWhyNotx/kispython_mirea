import re


def main(data_string):
    # ищем все значения опций в строке s
    pattern = r"@\s*'(\w+)'\s*<=\s*(-?\d+)\."
    matches = re.findall(pattern, data_string)
    # преобразуем найденные значения в список пар (name, value)
    result = [(match[0], int(match[1])) for match in matches]
    return result
