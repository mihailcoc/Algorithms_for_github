def partial_sorting(array, N):
    parts = 0
    maximum = 0
    for i in range(N):
        maximum = max(int(maximum), int(array[i]))
        if maximum == i:
            parts += 1
    return parts


def main():
    N = int(input())
    array = input().split()
    result = partial_sorting(array, N)
    print(result)


if __name__ == '__main__':
    main()
