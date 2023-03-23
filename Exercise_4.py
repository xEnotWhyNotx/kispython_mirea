# def main(n):
#     if n == 0:
#         return -0.48
#     elif n == 1:
#         return 0.23
#     else:
#         return 1 + (main(n - 2) ** 3) + main(n - 1)

# def main(n):
#     if n == 0:
#         return -0.48
#     elif n == 1:
#         return 0.23
#     return 1 + pow(main(n - 2), 3) + main(n - 1)

# def main(n):
#     return (-0.48 if n == 0
#             else 0.23 if n == 1
#             else 1 + main(n - 2) ** 3 + main(n - 1))


# def main(n):
#     return (
#         -0.48 if n == 0 else
#         0.23 if n == 1 else
#         1 + (main(n - 2) ** 3) + main(n - 1)
#     )

# def main(n):
#     return (
#         -0.48 if n == 0 else
#         0.23 if n == 1 else
#         (lambda x: 1 + x[0]**3 + x[1])([main(n-2), main(n-1)])
#     )


# def main(n):
#     sequence = [-0.48, 0.23]
#     for i in range(2, n + 1):
#         next_element = 1 + (sequence[i - 2] ** 3) + sequence[i - 1]
#         sequence.append(next_element)
#     return sequence[-1]


# def main(n):
#     a, b = -0.48, 0.23
#     for _ in range(n):
#         a, b = b, 1 + (a ** 3) + b
#     return a


# def main(n, a=-0.48, b=0.23):
#     return (
#         a if n == 0 else
#         b if n == 1 else
#         main(n - 1, b, 1 + (a ** 3) + b)
#     )


# def main(n):
#     cache = [-0.48, 0.23]
#     for i in range(2, n + 1):
#         result = 1 + cache[i - 2] ** 3 + cache[i - 1]
#         cache.append(result)
#     return cache[n]


# cache = [-0.48, 0.23]
#
#
# def main(n):
#     if n < len(cache):
#         return cache[n]
#     else:
#         result = 1 + main(n - 2) ** 3 + main(n - 1)
#         cache.append(result)
#         return result