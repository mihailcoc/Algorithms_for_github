def broken_search(n, nums, target):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    else:
        return -1


if __name__ == '__main__':
    n = int(input())
    target = int(input())
    arr = list(map(int, input().split()))
    index = broken_search(n, arr, target)
    print(index, sep='')


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6