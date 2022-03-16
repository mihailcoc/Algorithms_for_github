def several_inputs(n):
    coordinates = []
    for _ in range(0, n):
        new = sorted(list(map(int, input().split())))
        coordinates.append(new)
    return coordinates


def get_flower_beds(n, coordinates):
    coordinates.sort()
    result = [coordinates[0]]
    for i in range(1, n):
        right_result = result[len(result) - 1][1]
        if coordinates[i][0] <= right_result:
            result[len(result) - 1][1] = max(coordinates[i][1], right_result)
        else:
            result.append(coordinates[i])
    for _ in result:
        print(*_)


if __name__ == '__main__':
    n = int(input())
    coordinates = several_inputs(n)
    get_flower_beds(n, coordinates)

