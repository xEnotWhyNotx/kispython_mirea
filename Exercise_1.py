# import math
#
#
# def main(z, y):
#     result = math.sqrt(79 * ((y + 47 * (z ** 3)) ** 7) - 96 * (math.exp(31 * (y ** 2) - y)) ** 3) - \
#              80 * ((36 * (z ** 3) + (y / 32) + 1) ** 7)
#     return result

# import math
#
#
# def main(z, y):
#     return (79 * ((y + 47 * (z ** 3)) ** 7) - 96 * (math.exp(31 * (y ** 2) - y)) ** 3) ** 0.5 - \
#              80 * ((36 * (z ** 3) + (y / 32) + 1) ** 7)





#
#
# def main(z, y):
#     result = math.sqrt(79 * pow(y + 47 * pow(z, 3), 7) - 96 * pow(math.exp(31 * pow(y, 2) - y), 3) -
#                        80 * pow(((36 * pow(z, 3)) + (y / 32) + 1), 7))
#     return result


# def main(z, x):
#     result = math.sqrt(51 * ((9 * x - 42 * (z ** 3) - 1) ** 6)) - \
#              (69 * (math.sin(z) ** 7) - 63 * (math.cos(1 - 45 * (x ** 3)) ** 2))
#     return result
#
#
# print(main(-0.04, 0.31))


# def main(n, m, a, x):
#     summa = 0
#     for k in range(1, a + 1):
#         for i in range(1, m + 1):
#             for c in range(1, n + 1):
#                 summa += ((x ** 7) / 27) -\
#                     (((92 * (k ** 3) - c -
#                        (i ** 2)) ** 6) / 68) - 0.02
#     return summa
