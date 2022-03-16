if __name__ == '__main__':
    q = int(input())
    R = int(input())
    string = str(input())
    N = int(len(string))
    hash_summ = 0
    n = 1
    resultresult = 0
    for symbol in string:
        resultresult = (resultresult * q + ord(symbol)) % R
    print(resultresult)
