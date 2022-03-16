if __name__ == '__main__':
    M = input()
    first_array = [] * M
    first_array = input().split()
    find_symbols = []
    N = input()
    second_array = [] * N
    second_array = input().split()
    value = 0
    for symbol_in_first in first_array:
        # print(f'symbol_in_first {symbol_in_first}')
        for symbol_in_second in second_array:
            # print(f'symbol_in_second {symbol_in_second}')
            if symbol_in_first not in find_symbols:
                if symbol_in_first == symbol_in_second:
                    value = 1
                    find_symbols.append(symbol_in_first)
                    # print(f'find_symbols {find_symbols}')
                    # print(f'j {symbol_in_second}')
                    # print(f'value {value}')
                    # print(f'first_string[i-1:i] {first_string[i-1:i]}')
                    # print(f'second_string[i:i+1] {second_string[i:i+1]}')
                    # print(f'second_string[i-1:i] {second_string[i-1:i]}')
    print(value)