def check_index(array, middle, k, N, left, right):
    left = 0
    # right = 0
    count = 0
    for right in range(1, N, 1):
        # print(f' array[right] "{int(array[right])}"')
        # print(f' array[left] "{int(array[left])}"')
        while (int(array[right]) - int(array[left])) > int(middle):
            # print(f'int(array[right]) - int(array[left]) "{int(array[right]) - int(array[left])}"')
            # print(f'int(middle) "{int(middle)}"')
            left += 1
            # print(f'left "{left}"')
        count += right - left
        # print(f'count "{count}"')
        if count >= k:
            return True
    return False


def get_trash_index(array, k, N):
    left = 0
    right = int(array[N - 1]) - int(array[left])
    # print(f'right "{right}"')
    while int(left) < int(right):
        # print(f'int(left) "{int(left)}"')
        # print(f' int(right) "{int(right)}"')
        middle = int((right + left) / 2)
        # print(f'middle "{middle}"')
        if check_index(array, middle, k, N, left, right):
            # print(f'check_index(array, middle, k, N, left, right) "{check_index(array, middle, k, N, left, right)}"')
            right = middle
        else:
            left = middle + 1
    return left


if __name__ == '__main__':
    N = int(input())
    array = list()
    array = input().split()
    array = sorted(array)
    # print(array)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if int(array[j]) > int(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    # print(array)
    k = int(input())
    result = int(get_trash_index(array, k, N))
    # print(f' result "{result}"')
    print(result)
