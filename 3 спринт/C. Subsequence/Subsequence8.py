def subsequence(a, b):
    m = len(a)
    n = len(b)

    j = 0
    i = 0

    while j < m and i < n:
        if a[j] == b[i]:
            j = j + 1
        i = i + 1
    if j == m:
        return True
    return False


if __name__ == '__main__':
    a = input()
    b = input()
    print(subsequence(a, b))
