from struct import *

dictionary = dict(
    float1='f',
    double='d',
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q'
)


def parse(buffer, offset, type, order='<', _caller=None):
    pattern = dictionary[type]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buffer, offset)[0]
    return value, offset + size


def parse_a(buffer, offset):
    a1, offset = parse(buffer, offset, 'double', _caller=parse_a)
    a2, offset = parse_b(buffer, offset)
    return dict(A1=a1, A2=a2), offset


def parse_b(buffer, offset):
    b1 = ''
    for _ in range(6):
        value, offset = parse(buffer, offset, 'char', _caller=parse_b)
        b1 += value.decode()
    b2 = []
    for _ in range(3):
        value, offset = parse_c(buffer, offset)
        b2.append(value)
    offset_d, offset = parse(buffer, offset, 'uint32', _caller=parse_b)
    b3, _ = parse_d(buffer, offset_d)
    return dict(B1=b1, B2=b2, B3=b3), offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint16', _caller=parse_c)
    c2, offset = parse(buffer, offset, 'uint32', _caller=parse_c)
    c3, offset = parse(buffer, offset, 'double', _caller=parse_c)
    return dict(C1=c1, C2=c2, C3=c3), offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(4):
        value, offset = parse(buffer, offset, 'float1', _caller=parse_d)
        d1.append(value)
    size_d2, offset = parse(buffer, offset, 'uint32', _caller=parse_d)
    offset_d2, offset = parse(buffer, offset, 'uint32', _caller=parse_d)
    d2 = []
    for _ in range(size_d2):
        value, offset_d2 = parse(buffer, offset_d2, 'uint16', _caller=parse_d)
        d2.append(value)
    d3, offset = parse(buffer, offset, 'uint8', _caller=parse_d)
    return dict(D1=d1, D2=d2, D3=d3), offset


def main(data):
    return parse_a(data, 5)[0]
