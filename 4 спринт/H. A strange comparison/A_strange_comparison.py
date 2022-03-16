if __name__ == '__main__':
    first_string = []
    first_string = str(input())
    second_string = []
    second_string = str(input())
    M = len(first_string)
    N = len(second_string)
    value = 0
    if M == N:
        for i in range(1, M, 1):
            if (first_string[i] == first_string[i-1] and second_string[i] != second_string[i-1]) or (first_string[i] != first_string[i-1] and second_string[i] == second_string[i-1]):
                # print(f'iteration i {i}')
                # print(f'first_string[i:i+1] {first_string[i:i+1]}')
                # print(f'first_string[i-1:i] {first_string[i-1:i]}')
                # print(f'second_string[i:i+1] {second_string[i:i+1]}')
                # print(f'second_string[i-1:i] {second_string[i-1:i]}')
                value = 1
                break
        if value == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


