def quicksort(nums, left, right):
    starting_point = left
    ending_point = right
    right -= 1
    if left >= right:
        return nums
    pivot = nums[(left + right) // 2]
    while left < right:
        while left < right and nums[left] < pivot:
            left += 1
        while left < right and nums[right] > pivot:
            right -= 1
        if left != right:
            nums[left], nums[right] = nums[right], nums[left]

    quicksort(nums, starting_point, left)
    quicksort(nums, left + 1, ending_point)
    # return nums


if __name__ == '__main__':
    amount_of_members = int(input())
    members = [None] * amount_of_members
    for item in range(amount_of_members):
        member_info = input().split()
        members[item] = (-int(member_info[1]),
                         int(member_info[2]),
                         member_info[0])
    mas = quicksort(members, 0, amount_of_members)
    print(mas)
    print('\n'.join([i[-1] for i in mas]))