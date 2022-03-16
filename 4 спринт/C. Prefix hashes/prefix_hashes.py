if __name__ == '__main__':
    q = int(input())
    R = int(input())
    string = []
    string = str(input())
    qty_of_queries = int(input())
    first_index = int()
    last_index = int()
    result = 0
    for query in range(1, qty_of_queries + 1, 1):
        hash_summ = 0
        result = 0
        n = 1
        first_index, last_index = input().split()
        small_string = string[int(first_index) - 1:int(last_index)]
        for symbol in small_string:
            result = (result * q + ord(symbol)) % R
        print(result, sep='\n')
