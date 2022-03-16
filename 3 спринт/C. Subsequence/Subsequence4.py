def subsequence(a, b):
    x = -1
    m = []
    for symbol in a:
        x = b.find(symbol, x + 1)
        if x != -1:
            m.append(symbol[0])
    mm = set(m)
    aa = set(a)
    if mm == aa:
        return True
    else:
        return False


if __name__ == '__main__':
    a = input()
    b = input()
    print(subsequence(a, b))
