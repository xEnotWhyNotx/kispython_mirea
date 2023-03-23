from math import tan, cos


def main(n, b, x, m, a, y):
    summa = 0
    for c in range(1, b + 1):
        for i in range(1, n + 1):
            summa += 35 * ((89 * (x ** 2) - 75 *
                            (c ** 3)) ** 6) - (tan(i) / 51)
    for k in range(1, a + 1):
        for i in range(1, b + 1):
            for j in range(1, m + 1):
                summa += ((y - (k ** 3)) ** 7) - (cos(j) ** 5) - i ** 4
    return summa
