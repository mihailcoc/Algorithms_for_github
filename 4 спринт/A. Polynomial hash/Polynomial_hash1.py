if __name__ == '__main__':
    q = int(input())
    R = int(input())
    string = str(input())
    N = int(len(string))
    hash_summ = 0
    n = 1
    result = 0
    for symbol in string:
        meaning_of_symbol = ord(symbol)
        hash_summ = hash_summ + (meaning_of_symbol * q**(N - n))
        n += 1
    result = hash_summ % R
    print(result)
