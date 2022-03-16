def getMaxUnigueStringLen(s):
    chec_l = {}
    index_str = 0
    length = 0
    for i, v in enumerate(s):
        if v in chec_l:
            index_str = max(index_str, chec_l[v] + 1)
        chec_l[v] = i
        length = max(length, i - index_str + 1)
    return length


if __name__ == '__main__':
    string = []
    string = str(input())
    res = getMaxUnigueStringLen(string)
    print(res)
