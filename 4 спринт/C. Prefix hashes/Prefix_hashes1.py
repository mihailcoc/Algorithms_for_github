if __name__ == '__main__':
    q = int(input())
    R = int(input())
    string = []
    string = str(input())
    qty_of_queries = int(input())
    first_index = int()
    last_index = int()
    for query in range(1, qty_of_queries + 1, 1):
        hash_summ = 0
        n = 1
        print(f'query "{query}"')
        first_index, last_index = input().split()
        print(f'first_index "{first_index}"')
        print(f'last_index "{last_index}"')
        small_string = string[int(first_index) - 1:int(last_index)]
        print(f'small_string "{small_string}"')
        for symbol in small_string:
            N = int(len(small_string))
            print(f'symbol "{symbol}"')
            meaning_of_symbol = ord(str(symbol))
            print(f'meaning_of_symbol "{meaning_of_symbol}"')
            hash_summ = hash_summ + (meaning_of_symbol * q**(N - n))
            print(f'hash_summ "{hash_summ}"')
            n += 1
        result = hash_summ % R
        print(result, sep='\n')
