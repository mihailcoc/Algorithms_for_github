if __name__ == '__main__':
    q = int(input())
    R = int(input())
    string = []
    string = str(input())
    N = len(string)
    qty_of_queries = int(input())
    first_index = int()
    last_index = int()
    result = 0
    hash_prefix_array = [] * N
    hash_prefix_array = [(int(ord(string[i])) % R) for i in range(0, N, 1)]
    # print(f'hash_perfix_array "{hash_prefix_array}"')
    for query in range(1, qty_of_queries + 1, 1):
        # print(f'query "{query}"')
        hash_summ = 0
        result = 0
        n = 1
        first_index, last_index = input().split()
        for i in range(int(first_index) - 1, int(last_index), 1):
            # print(f'i "{i}"')
            # print(f'int(first_index) "{int(first_index)}"')
            # print(f'int(last_index) "{(int(last_index))}"')
            result = (result * q) % R + hash_prefix_array[i]
            # result1 = (hash_prefix_array[i]) % R
            # result2 = (result * q) % R
            # print(f'hash_perfix_array[i] "{hash_prefix_array[i]}"')
            # print(f'result1 % R "{result1}"')
            # print(f'result * q "{q}" % R "{R}" "{result2}"')
        print(result, sep='\n')
