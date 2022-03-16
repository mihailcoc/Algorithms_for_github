def subsequence(a, b):
    y = -1
    m = []
    for symbol in a:
        y = b.find(symbol, y + 1)
        if y != -1:
            m.append(symbol[0])
    res = [symbol for symbol in a if symbol not in m]
    if not res:
        return True
    else:
        return False


if __name__ == '__main__':
    a = []
    b = []
    a = input()
    b = input()
    print(subsequence(a, b))
