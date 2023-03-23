# # s = (
# #     {2015, "HY", "RUBY"},
# #     {2015, "HY", "SAGE"},
# #     {2015, "HY", "XS"},
# #     {2015, 'STON'},
# #     {2001, "RUBY", "NL", 1960},
# #     {2001, "RUBY", "NL", 1988},
# #     {2001, "RUBY", "CSS", 1960},
# #     {2001, "RUBY", "CSS", 1988},
# #     {2001, "SAGE", "NL"},
# #     {2001, "SAGE", "CSS", 1960},
# #     {2001, "SAGE", "CSS", 1988},
# #     {2001, "XS"},
# #     {2003},
# # )
# #
# #
# # def main(r):
# #     s1 = set(r)
# #     return [i for i in range(len(s)) if not (len(s[i] - s1))][0]
#
#
# # s = [
# #     {2015, "HY", "RUBY"},
# #     {2015, "HY", "SAGE"},
# #     {2015, "HY", "XS"},
# #     {2015, 'STON'},
# #     {2001, "RUBY", "NL", 1960},
# #     {2001, "RUBY", "NL", 1988},
# #     {2001, "RUBY", "CSS", 1960},
# #     {2001, "RUBY", "CSS", 1988},
# #     {2001, "SAGE", "NL"},
# #     {2001, "SAGE", "CSS", 1960},
# #     {2001, "SAGE", "CSS", 1988},
# #     {2001, "XS"},
# #     {2003},
# # ]
# #
# #
# # def main(r):
# #     s1 = set(r)
# #     for i, v in enumerate(s):
# #         if not (len(v - s1)):
# #             return i
#
#
# s = [
#     {2015, "HY", "RUBY"},
#     {2015, "HY", "SAGE"},
#     {2015, "HY", "XS"},
#     {2015, 'STON'},
#     {2001, "RUBY", "NL", 1960},
#     {2001, "RUBY", "NL", 1988},
#     {2001, "RUBY", "CSS", 1960},
#     {2001, "RUBY", "CSS", 1988},
#     {2001, "SAGE", "NL"},
#     {2001, "SAGE", "CSS", 1960},
#     {2001, "SAGE", "CSS", 1988},
#     {2001, "XS"},
#     {2003},
# ]
#
#
# def main(r):
#     s1 = set(r)
#     for i, v in enumerate(s):
#         if set(v).issubset(s1):
#             return i


# def zero(items, left, right):
#     if items[0] == 'HY':
#         return right
#     if items[0] == 'STON':
#         return left
#
#
# def one(items, left, middle, right):
#     if items[1] == 2015:
#         return right
#     if items[1] == 2001:
#         return middle
#     if items[1] == 2003:
#         return left
#
#
# def two(items, left, middle, right):
#     if items[2] == 'RUBY':
#         return right
#     if items[2] == 'SAGE':
#         return middle
#     if items[2] == 'XS':
#         return left
#
#
# def three(items, left, right):
#     if items[3] == 1960:
#         return right
#     if items[3] == 1988:
#         return left
#
#
# def four(items, left, right):
#     if items[4] == "NL":
#         return right
#     if items[4] == "CSS":
#         return left
#
#
# def main(items):
#     return one(
#         items,
#         12,
#         two(
#             items, 11, four(
#                 items,
#                 three(
#                     items,
#                     10,
#                     9),
#                 8
#             ),
#             four(
#                 items,
#                 three(
#                     items,
#                     7,
#                     6), three(
#                     items,
#                     5,
#                     4))
#         ),
#         zero(
#             items,
#             3,
#             two(
#                 items,
#                 2,
#                 1,
#                 0)
#         ),
#     )


def zero(items, left, right):
    if items[0] == 'HY':
        return right
    if items[0] == 'STON':
        return left


def one(items, left, middle, right):
    if items[1] == 2015:
        return right
    if items[1] == 2001:
        return middle
    if items[1] == 2003:
        return left


def two(items, left, middle, right):
    if items[2] == 'RUBY':
        return right
    if items[2] == 'SAGE':
        return middle
    if items[2] == 'XS':
        return left


def three(items, left, right):
    if items[3] == 1960:
        return right
    if items[3] == 1988:
        return left


def four(items, left, right):
    if items[4] == "NL":
        return right
    if items[4] == "CSS":
        return left


def main(items):
    result = one(
        items,
        12,
        two(
            items, 11, four(
                items,
                three(
                    items,
                    10,
                    9),
                8
            ),
            four(
                items,
                three(
                    items,
                    7,
                    6), three(
                    items,
                    5,
                    4))
        ),
        zero(
            items,
            3,
            two(
                items,
                2,
                1,
                0)
        ),
    )
    return result
