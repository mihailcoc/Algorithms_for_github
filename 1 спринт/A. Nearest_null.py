# ID 54992335
# https://contest.yandex.ru/contest/23390/problems/A/?success=54992335#51450/2020_11_13/VxxSc5X0LZ


def nearest_null(n, street):

    null_address = [0] * len(street)
    null_address_last = null_address_first = street.index(0)

    for street_position in range(null_address_first, len(street)):
        if street[street_position] != 0:
            null_address[street_position] = null_address[street_position-1] + 1
        else:
            null_address_last = street_position

    for street_position in range(null_address_last, null_address_first, -1):
        null_address[street_position] = 0 if street[
            street_position] == 0 else min(null_address[
                street_position], null_address[street_position+1] + 1)

    for street_position in range(null_address_first-1, -1, -1):
        null_address[street_position] = null_address[street_position+1] + 1

    return null_address


if __name__ == '__main__':
    n = int(input())
    street = list(map(int, input().split()))
    print(*nearest_null(n, street))
