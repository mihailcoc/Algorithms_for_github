def subsequence(a, b):
    x = -1
    m = []
    for symbol in a:
        x = b.find(symbol, x + 1)
        if x != -1:
            m.append(symbol[0])
    mm = set(m)
    print(mm)
    aa = set(a)
    print(aa)
    if mm == aa:
        print(f'm {m}')
        print(*m)
        print(f'a {a}')
        print(f'b {b}')
        return True
    else:
        print(m)
        print(*m)
        print(a)
        print(b)
        return False


if __name__ == '__main__':
    a = input()
    b = input()
    print(subsequence(a, b))
