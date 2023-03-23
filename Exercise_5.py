# import math
#
#
# def main(z, y):
#     summa = 0
#     for i in range(1, len(z) + 1):
#         summa += \
#             (math.cos(y[math.ceil(i / 4) - 1] +
#                       (z[math.ceil(i / 4) - 1]) ** 3 +
#                       8 * (z[(len(z) + 1) -
#                              math.ceil(i / 3) - 1]) ** 2)) ** 7 / 84
#     return 98 * summa

# from math import cos, ceil
#
#
# def main(z, y):
#     summa = 0
#     for i in range(1, len(z) + 1):
#         summa += \
#             (cos(y[ceil(i / 4) - 1] +
#                  (z[ceil(i / 4) - 1]) ** 3 +
#                  8 * (z[(len(z) + 1) -
#                         ceil(i / 3) - 1]) ** 2)) ** 7 / 84
#     return 98 * summa


# import math
#
#
# def main(z, y):
#     return 98 * sum([(math.cos(y[(i-1)//4] +
#                                z[(i-1)//4]**3 +
#                                8*z[len(z)-(i-1)//3-1]**2))**7 / 84
#                      for i in range(1, len(z)+1)])


# import math
#
#
# def main(z, y):
#     return 98 * sum(map(lambda i: (math.cos(y[(i - 1) // 4] +
#                                             z[(i - 1) // 4] ** 3 +
#                                             8 * z[len(z) -
#                                                   (i - 1) // 3 -
#                                                   1] ** 2)) ** 7 / 84,
#                         range(1, len(z) + 1)))


# from math import cos
#
#
# def main(z, y):
#     return 98 * sum([(cos(y[(i - 1) // 4] +
#                           z[(i - 1) // 4] ** 3 +
#                           8 * z[len(z) - (i - 1) // 3 - 1] ** 2)) ** 7 / 84
#                      for i in range(1, len(z) + 1)])


# import math
# from functools import reduce
#
#
# def main(z, y):
#     summands = [(math.cos(y[(i - 1) // 4] +
#                           z[(i - 1) // 4] ** 3 +
#                           8 * z[len(z) -
#                                 (i - 1) // 3 - 1] ** 2)) ** 7 / 84 for
#                 i in range(1, len(z) + 1)]
#     return 98 * reduce(lambda x, y: x + y, summands)


# import math
#
#
# def main(z, y):
#     values = list(map(lambda i:
#                       (math.cos(y[math.ceil(i / 4)
#                                   - 1] +
#                                 (z[math.ceil(i / 4)
#                                    - 1]) ** 3
#                                 + 8 * (z[(len(z) + 1)
#                                          - math.ceil(i / 3)
#                                          - 1]) ** 2)) ** 7 / 84,
#                       range(1, len(z) + 1)))
#     return 98 * sum(values)


import math


def main(z, y):
    n = len(z)
    y.insert(0, 0)
    z.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        left = y[math.ceil(i / 4)]
        middle = z[math.ceil(i / 4)] ** 3
        right = 8 * z[n + 1 - math.ceil(i / 3)] ** 2
        total += (math.cos(left + middle + right) ** 7) / 84
    return 98 * total
