def quick_sort(data, left, right):
    if right - left < 2:
        return data
    mid = (left + right) // 2
    pivot = data[mid]
    start, end = left, right
    while start < end:
        while data[start] < pivot:
            start += 1
        while pivot < data[end]:
            end -= 1
        data[start], data[end] = data[end], data[start]
        start += 1
        end -= 1
    quick_sort(data, left, start)
    quick_sort(data, start + 1, right)
    result = [value[2] for value in data]
    return result


if __name__ == '__main__':
    def participant(name, score, penalty):
        return [- int(score), int(penalty), name]
    amount = int(input())
    print('\n'.join(quick_sort(
        [participant(*input().split()) for _ in range(amount)],
        0,
        amount - 1
    )))