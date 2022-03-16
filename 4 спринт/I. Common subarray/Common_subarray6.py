import hashlib

hash = hashlib.shake_256()


def GetHash(item):
    bytes_str = item.encode()
    return hashlib.shake_256(bytes_str).hexdigest(15)


def GetLCS(first_array, second_array):
    value = 0
    for i in range(0, int(M), 1):
        # print(f'first_array[i] {first_array[i]}')
        for j in range(0, int(N), 1):
            first_array_hash1 = GetHash(first_array[i])
            # print(f'first_array_hash1 {first_array_hash1}')
            second_array_hash1 = GetHash(second_array[j])
            # print(f'second_array_hash1 {second_array_hash1}')
            if first_array_hash1 == second_array_hash1:
                # print(f'second_array[j] {second_array[j]}')
                # find_symbols.append(first_array[i])
                # print(f'find_symbols {find_symbols}')
                first_array_hash2 = GetHash(first_array[i - 1])
                # print(f'first_array_hash2 {first_array_hash2}')
                second_array_hash2 = GetHash(second_array[j - 1])
                # print(f'second_array_hash2 {second_array_hash2}')
                if first_array_hash2 == second_array_hash2:
                    # print(f'first_array[i - 1] {first_array[i - 1]}')
                    # print(f'second_array[j - 1] {second_array[j - 1]}')
                    value += 1
                    # print(f'value += 1 {value}')
                else:
                    value = 1
                    # print(f'value = 1 {value}')
    return value


if __name__ == '__main__':
    M = int(input())
    left_array = [] * M
    left_array = input().split()
    N = int(input())
    right_array = [] * N
    right_array = input().split()
    res = GetLCS(left_array, right_array)
    print(res)