def subsequence(a, b):
    x = -1
    while x != -1:
        for symbol in a:
            x = b.find(symbol, x + 1)
            print(symbol)
            print(x)
        return True
    return False


if __name__ == '__main__':
    a = input()
    b = input()
    print(subsequence(a, b))
