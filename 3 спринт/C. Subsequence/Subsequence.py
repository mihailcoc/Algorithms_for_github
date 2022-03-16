def subsequence1(a, b):
    y = 0
    for symbol in a:
        y = b.find(symbol, y)
        if y == -1:
            return False
    else:
        return True


if __name__ == '__main__':
    a = input()
    b = input()
    print(subsequence1(a, b))

