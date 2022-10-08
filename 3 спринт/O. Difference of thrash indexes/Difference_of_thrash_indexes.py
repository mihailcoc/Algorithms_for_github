def check_index(data, pos, k):
    left = 0
    right = 0
    count = 0
    for right in range(1, len(data)):
        while data[right] - data[left] > pos:
            left += 1
        count += right - left
        if count >= k:
            return True
    return False


def get_trash_index(data, k):
    left = 0
    right = data[-1] - data[left]
    while left < right:
        middle = (right + left) // 2
        if check_index(data, middle, k):
            right = middle
        else:
            left = middle + 1
    return left


if __name__ == '__main__':
    _ = input()
    islands = [int(i) for i in input().split()]
    k = int(input())
    print(get_trash_index(sorted(islands), k))
