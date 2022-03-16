def check_index(data, pos, k):
    left = 0
    right = 0
    count = 0
    for right in range(1, len(data)):
        # print(f' array[right] "{int(array[right])}"')
        # print(f' array[left] "{int(array[left])}"')
        while data[right] - data[left] > pos:
            # print(f'int(array[right]) - int(array[left]) "{int(array[right]) - int(array[left])}"')
            # print(f'int(middle) "{int(middle)}"')
            left += 1
            # print(f'left "{left}"')
        count += right - left
        # print(f'count "{count}"')
        if count >= k:
            return True
    return False


def get_trash_index(data, k):
    left = 0
    right = data[-1] - data[left]
    # print(f'right "{right}"')
    while left < right:
        # print(f'int(left) "{int(left)}"')
        # print(f' int(right) "{int(right)}"')
        middle = (right + left) // 2
        # print(f'middle "{middle}"')
        if check_index(data, middle, k):
            # print(f'check_index(array, middle, k, N, left, right) "{check_index(array, middle, k, N, left, right)}"')
            right = middle
        else:
            left = middle + 1
    return left


if __name__ == '__main__':
    _ = input()
    islands = [int(i) for i in input().split()]
    k = int(input())
    print(get_trash_index(sorted(islands), k))
