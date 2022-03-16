def quicksort(data, left, right):
    if right <= left:
        return
    else:
        # recursive case
        pivot = partition(data, left, right)
        print(f'pivot{pivot}')
        quicksort(data, left, pivot-1)
        quicksort(data, pivot+1, right)
    return data


def partition(data, left, right):
    pivot = data[left]
    lIndex = left + 1
    rIndex = right
    while True:
        while lIndex <= rIndex and data[lIndex] <= pivot:
            lIndex += 1
        while rIndex >= lIndex and data[rIndex] >= pivot:
            rIndex -= 1
        if rIndex <= lIndex:
            break
        data[lIndex], data[rIndex] = data[rIndex], data[lIndex]
        print(data)
    data[lIndex], data[rIndex] = data[rIndex], data[lIndex]
    print(data)
    return rIndex


if __name__ == '__main__':
    def participant(name, task, mistake):
        return -int(task), int(mistake), name
    a = int(input())
    result = (login for _, _, login in quicksort(
        [participant(*input().split()) for _ in range(a)], 0, a - 1
    ))
    print(*result, sep="\n")
