# def main(hex_string):
#     # Преобразовать шестнадцатиричную строку в целое число.
#     num = int(hex_string, 16)
#
#     # Применить битовую операцию И (&) с маской, чтобы сохранить только необходимые биты.
#     mask = 0xFFFFF000
#     bits = num & mask
#
#     # Применить битовую операцию ИЛИ (|) с новым значением для битового поля.
#     new_bits = 0x1A000
#     result = bits | new_bits
#
#     # Преобразовать целое число обратно в шестнадцатиричную строку.
#     return hex(result)


# def main(hex_string):
#     # Преобразовать шестнадцатиричную строку в целое число.
#     num = int(hex_string, 16)
#
#     # Применить битовую операцию И (&) с маской, чтобы сохранить только необходимые биты.
#     mask = 0xFFFFFFFF
#     bits = num & mask
#
#     # Применить битовую операцию ИЛИ (|) с новым значением для битового поля.
#     new_bits = 0x1A000
#     result = bits | new_bits
#
#     # Преобразовать целое число обратно в шестнадцатиричную строку.
#     return hex(result)


def main(hex_string):
    bin_string1 = bin(int(hex_string, 16))
    bin_string = bin_string1[2:]
    if len(bin_string) < 23:
        for i in range(23 - len(bin_string)):
            bin_string = '0' + bin_string
    o5 = int(bin_string[0], 2)
    o4 = int(bin_string[1], 2)
    o3 = int(bin_string[2:12], 2)
    o2 = int(bin_string[12:16], 2)
    o1 = int(bin_string[16:23], 2)
    hex_string = hex((o2 << 19) | (o1 << 12) | (o4 << 11) | (o5 << 10) | o3)
    return hex_string


print(main("0x3f9b8c"))

# def main(input):
#     hex_number = input  # Входное шестнадцатеричное число
#     decimal_number = int(hex_number, 16)  # Преобразование шестнадцатеричного числа в десятичное число
#     bin_num = bin(decimal_number)
#     a = (bin_num & 0b10000000000000000000000)
#     b = (bin_num & 0b01000000000000000000000)
#     c = (bin_num & 0b00111111111100000000000)
#     d = (bin_num & 0b00000000000011110000000)
#     e = (bin_num & 0b00000000000000001111111)
#     return a | b | c | d | e
# print(main("0x5a483b"))
