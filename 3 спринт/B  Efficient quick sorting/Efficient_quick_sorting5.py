def quick_sort(data, start: int, end: int):
    def partition(start: int, end: int):
        if start >= end:
            return
        pivot = start
        for item in range(start, end):
            if data[end] > data[item]:
                data[pivot], data[item] = data[item], data[pivot]
                pivot += 1
        data[pivot], data[end] = data[end], data[pivot]
        partition(start, pivot - 1)
        partition(pivot + 1, end)
    partition(0, len(data) - 1)
    return data


if __name__ == '__main__':
    def people(name, task: int, score: int):
        return -int(task), int(score), name
    n = int(input())
    array = [people(*input().split()) for _ in range(n)]
    result = (login for _, _, login in quick_sort(array, 0, n - 1))
    print(*result, sep="\n")
