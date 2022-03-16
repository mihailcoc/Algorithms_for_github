import functools


def subsequence(a, b):
    z = -1
    m = []
    for symbol in a:
        z = b.find(symbol, z + 1)
        if z != -1:
            m.append(symbol[0])
    if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, m, a), True):
        return True
    else:
        return False


if __name__ == '__main__':
    a = []
    b = []
    a = input()
    b = input()
    print(subsequence(a, b))
