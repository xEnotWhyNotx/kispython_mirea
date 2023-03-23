# import math
#
#
# def main(y):
#     if y < 35:
#         return y + 34 + 66 * ((20 * (y ** 2)) ** 5)
#     elif 35 <= y < 105:
#         return y ** 2
#     elif 105 <= y < 166:
#         return 1 - 77 * (y ** 2)
#     elif 166 <= y < 228:
#         return (y ** 4) + ((y ** 7) / 74)
#     elif y > 228:
#         return 1 + 64 * (math.log(y, 10) ** 4) + 74 * (47 - 53 * (y ** 3))


#
# from math import log
#
#
# def main(y):
#     if y < 35:
#         return y + 34 + 66 * ((20 * (y ** 2)) ** 5)
#     elif 35 <= y < 105:
#         return y ** 2
#     elif 105 <= y < 166:
#         return 1 - 77 * (y ** 2)
#     elif 166 <= y < 228:
#         return (y ** 4) + ((y ** 7) / 74)
#     elif y > 228:
#         return 1 + 64 * (log(y, 10) ** 4) + 74 * (47 - 53 * (y ** 3))


# import math
#
#
# def main(y):
#     if y < 35:
#         return y + 34 + 66 * ((20 * (y ** 2)) ** 5)
#     elif y < 105:
#         return y ** 2
#     elif y < 166:
#         return 1 - 77 * y ** 2
#     elif y < 228:
#         return y ** 4 + y ** 7 / 74
#     else:
#         return 1 + 64 * math.log(y, 10) ** 4 + 74 * (47 - 53 * y ** 3)


# import math
#
#
# def main(y):
#     return (
#         y + 34 + 66 * ((20 * (y ** 2)) ** 5) if y < 35 else
#         y ** 2 if y < 105 else
#         1 - 77 * y ** 2 if y < 166 else
#         y ** 4 + y ** 7 / 74 if y < 228 else
#         1 + 64 * math.log(y, 10) ** 4 + 74 * (47 - 53 * y ** 3)
#     )
