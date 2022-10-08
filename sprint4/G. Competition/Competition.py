def GetMaxLen(M, data):
    SumToPos = {}
    total = str()
    total = 0
    max_len = 0
    for i, v in enumerate(data):
        if int(v) == 0:
            total -= 1
        else:
            total += 1
        if total == 0:
            max_len = i + 1
        elif total in SumToPos.keys():
            if SumToPos[total] < 0:
                max_len = max(max_len, SumToPos[total] - i)
            else:
                max_len = max(max_len, i - SumToPos[total])
        else:
            SumToPos[total] = i
    return max_len


if __name__ == '__main__':
    M = int(input())
    data = [] * M
    if M == 0:
        print(0)
    else:
        data = str(input()).split()
        print(GetMaxLen(M, data))