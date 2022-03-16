def binary_search(nums, target):
    low = 0
    hight = len(nums)-1

    while low <= hight:
        mid = (low + hight) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            hight = mid - 1
        else:
            low = mid + 1
    return -1


def search_fault(nums):
    if nums[0] < nums[-1]:
        return -1

    low = 0
    hight = len(nums)-1

    while hight - low >= 2:
        mid = (low + hight) // 2
        if nums[low] > nums[mid]:
            hight = mid
        else:
            low = mid
    return low


def broken_search(nums, target) -> int:
    if len(nums) == 0:
        return -1

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    fault = search_fault(nums)
    if fault == -1 and nums[0] <= target <= nums[-1]:
        return binary_search(nums, target)

    if nums[fault] == target:
        return fault

    if nums[0] <= target <= nums[fault-1]:
        return binary_search(nums[0: fault], target)

    if nums[fault+1] <= target <= nums[-1]:
        index = binary_search(nums[fault+1: len(nums)], target)
        if index != -1:
            return index + fault + 1

    return -1