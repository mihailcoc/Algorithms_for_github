def several_inputs(n):
    arr = []
    for _ in range(0, n):
        new = sorted(list(map(int, input().split())))
        arr.append(new)
    return arr


def segments(arr):
    new_arr = []
    new_arr.append(arr[0])
    new_segment = new_arr[0]
    for _ in range(1, len(arr)):
        segment = arr[_]
        # 1
        if (
                new_segment[0] <= segment[0] and
                new_segment[-1] >= segment[-1]
        ):
            continue
        # 2
        elif (
                new_segment[0] >= segment[0] and
                new_segment[-1] <= segment[-1]
        ):
            new_segment[0] = segment[0]
            new_segment[-1] = segment[-1]
        # 3
        elif (
                new_segment[0] <= segment[0] <= new_segment[-1] and
                segment[0] <= new_segment[-1] <= segment[-1]
        ):
            new_segment[-1] = segment[-1]
        # 4
        elif (
                segment[0] <= new_segment[0] <= segment[-1] and
                new_segment[0] <= segment[-1] <= new_segment[-1]
        ):
            new_segment[0] = segment[0]

        else:
            new_arr.append(arr[_])

        if new_segment[0] > segment[0] and new_segment[0] > segment[-1]:
            temporary = new_arr[0]
            new_arr[0] = arr[_]
            new_arr[1] = temporary
    # res = new_arr
    # print(res)
    for _ in new_arr:
        res = ' '.join([str(e) for e in _])
        print(res)


if __name__ == '__main__':
    n = int(input())
    x = several_inputs(n)
    # print(x)
    segments(x)