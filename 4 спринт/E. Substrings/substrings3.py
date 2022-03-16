def getMaxUnigueStringLen(string):
    symbol = str()
    value = int()
    value = 0
    letter_to_pos = {symbol: value}
    result = int()
    prev = int()
    prev = 0
    for i in range(len(string)):
        symbol = string[i]
        print(f'i "{i}" ')
        print(f'symbol "{symbol}" ')
        letter_to_pos[string[i]] = value
        print(f'value "{value}" ')
        prev = max(prev, value)
        print(f'prev "{prev}" ')
        letter_to_pos[string[i]]  = int(i + 1)
        print(f'value "{value}" ')
        result = max(result, ((i + 1) - prev))
        print(f'result  "{result}" ')
    return result


if __name__ == '__main__':
    string = []
    string = str(input())
    res = getMaxUnigueStringLen(string)
    print(res)
