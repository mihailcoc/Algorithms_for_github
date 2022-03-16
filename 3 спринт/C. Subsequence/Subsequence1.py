def subsequence(a, b):
    x = -1
    for symbol in a:
        x = b.find(symbol, x + 1)
        if x != -1:
            return True
        else:
            return False


if __name__ == '__main__':
    a = input()
    b = input()
    print(subsequence(a, b))
