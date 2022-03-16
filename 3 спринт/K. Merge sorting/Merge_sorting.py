def merge(array, left, mid, right):
    left_array = array[left:mid]
    right_array = array[mid:right]
 
    k = left
    left_index = 0
    right_index = 0
    while (left + left_index < mid and mid + right_index < right):
        if (left_array[left_index] <= right_array[right_index]):
            array[k] = left_array[left_index]
            left_index = left_index + 1
        else:
            array[k] = right_array[right_index]
            right_index = right_index + 1
        k = k + 1
    if left + left_index < mid:
        while k < right:
            array[k] = left_array[left_index]
            left_index = left_index + 1
            k = k + 1
        return array
    else:
        while k < right:
            array[k] = right_array[right_index]
            right_index = right_index + 1
            k = k + 1
        return array
 
    # left_index, right_index, result_index = 0, 0, 0
    # while left_index < len(left_array) and right_index < len(right_array):
    #     if left_array[left_index] <= right_array[right_index]:
    #         result[result_index] = left_array[left_index]
    #         left_index += 1
    #     else:
    #         result[result_index] = right_array[right_index]
    #         right_index += 1
    #     result_index += 1
 
    # while left_index < len(left_array):
    #     result[result_index] = left_array[left_index]
    #     left_index += 1
    #     result_index += 1
    # while right_index < len(right_array):
    #     result[result_index] = right_array[right_index]
    #     right_index += 1
    #     result_index += 1
    # return result
 
 
def merge_sort(array, left, right):
    mid = (left + right) // 2
    if right - left > 2:
        merge_sort(array, left, mid)
        merge_sort(array, mid, right)
 
    result = merge(array, left, mid, right)


def test_b():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    print('b: ', b)
    print('expected', expected)
    assert b == expected
