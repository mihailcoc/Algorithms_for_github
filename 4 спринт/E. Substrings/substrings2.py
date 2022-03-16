def getMaxUnigueStringLen(string):
    print(f'string  "{string}" ')
    symbol = str()
    value = int()
    value = 0
    letter_to_pos = {symbol: value}
    small_string = []
    result = int()
    prev = int()
    prev = 0
    for i in range(len(string)):
        print(f'i "{i}" ')
        symbol = string[i]
        print(f'symbol "{symbol}" ')
        if symbol in small_string:
            prev = letter_to_pos[string[i]]
            print(f'if prev "{prev}" ')
            small_string = []
            print(f'if small_string "{small_string}" ')
            letter_to_pos[string[i]] = value
            print(f'value "{value}" ')
            prev = max(prev, value)
            print(f'prev "{prev}" ')
            letter_to_pos[string[i]] = int(i + 1)
            print(f'value "{value}" ')
            result = max(result, ((i + 1) - prev))
            print(f'result  "{result}" ')
        else:
            small_string.append(symbol)
            print(f'else small_string "{small_string}" ')
            letter_to_pos[string[i]] = value
            print(f'value "{value}" ')
            prev = max(prev, value)
            print(f'prev "{prev}" ')
            letter_to_pos[string[i]] = int(i + 1)
            print(f'value "{value}" ')
            result = max(result, ((i + 1) - prev))
            print(f'result  "{result}" ')
        for r in range(prev, i, 1):
            print(f'r "{r}" ')
            print(f'i "{i}" ')
            print(f'prev "{prev}" ')
            symbol = string[r]
            print(f'symbol"{symbol}" ')
            small_string.append(symbol)
            print(f'append small_string "{small_string}" ')
    return result


if __name__ == '__main__':
    string = []
    string = str(input())
    res = getMaxUnigueStringLen(string)
    print(res)
