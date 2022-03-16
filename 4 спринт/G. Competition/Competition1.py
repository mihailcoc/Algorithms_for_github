def GetMaxLen(M, data):
    SumToPos = {}
    total = str()
    total = 0
    max_len = 0
    print(f'data {data}')
    for i, v in enumerate(data):
        print(f'step1 [i] {i}')
        print(f'step1 int(v) {int(v)}')
        if int(v) == 0:
            print(f'step1 v == 0 {int(v)}')
            total -= 1
            print(f'step1 total -= 1 {total}')
        else:
            print(f'step1 v == 1 {int(v)}')
            total += 1
            print(f'step1 total += 1 {total}')
        if total == 0:
            print(f'step2 total {total}')
            max_len = i + 1
            print(f'step2 max_len {max_len}')
        elif total in SumToPos.keys():
            print(f'step3 elif [i] {i}')
            print(f'step3 elif max_len {max_len}')
            print(f'step3 elif SumToPos[total] {SumToPos[total]}')
            print(f'step3 elif i - SumToPos[total] {i - SumToPos[total]}')
            if SumToPos[total] < 0:
                max_len = max(max_len, SumToPos[total] - i)
            else:
                max_len = max(max_len, i - SumToPos[total])
            print(f'step3  elif max_len {max_len}')
        else:
            print(f'step3 else [i] {i}')
            print(f'step1 v == 1 {int(v)}')
            print(f'step3 else total {total}')
            print(f'step3 else SumToPos {SumToPos}')
            SumToPos[total] = i
            print(f'step3 else SumToPos[total] {SumToPos[total]}')
            print(f'step3 else SumToPos {SumToPos}')
    return max_len


if __name__ == '__main__':
    M = int(input())
    data = [] * M
    if M == 0:
        print(0)
    else:
        data = str(input()).split()
        print(GetMaxLen(M, data))
