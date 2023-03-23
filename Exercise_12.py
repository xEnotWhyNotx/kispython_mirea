import operator


def main(U):
    c = {7 * elem - abs(elem) for elem
         in U if elem > -3 or elem < -6}
    d = {elem / 2 - 7 * elem for elem
         in U if operator.xor(elem > 0, elem < -5)}
    return len(d) - sum(c)
print(main([0.99, 7.8, -8.65, 0.61, 4.31]))
