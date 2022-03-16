def several_inputs(n):
    coordinates = []
    for _ in range(0, n):
        new = sorted(list(map(int, input().split())))
        coordinates.append(new)
    return coordinates


def get_flower_beds(n, coordinates):
    coordinates.sort()
    print(f'сортированный массив "{coordinates}" ')
    result = [coordinates[0]]
    for i in range(1, n):
        print(f'итерация "{i}" ')
        right_result = result[len(result) - 1][1]
        if coordinates[i][0] <= right_result:
            print(f'coordinates[i][0] "{coordinates[i][0]}" ')
            print(f'right_result "{right_result}" ')
            result[len(result) - 1][1] = max(coordinates[i][1], right_result)
            print(f'max(coordinates[i][1], right_result) "{max(coordinates[i][1], right_result)}" ')
        else:
            result.append(coordinates[i])
            print(f'coordinates[i] "{coordinates[i]}" ')
    for _ in result:
        print(*_)


if __name__ == '__main__':
    n = int(input())
    coordinates = several_inputs(n)
    get_flower_beds(n, coordinates)

