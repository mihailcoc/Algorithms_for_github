ID 54683761
https://contest.yandex.ru/contest/23390/problems/A/?success=54683761#51450/2020_11_13/VxxSc5X0LZ


def nearest_null(n, street):

    null_address = [0] * len(street)
    null_address_first = street.index(0)
    null_address_last = street.index(0)

    for street_position in range(null_address_first, len(street)):
        if street[street_position] != 0:
            null_address[street_position] = null_address[street_position-1] + 1
        else:
            null_address_last = street_position

    for street_position in range(null_address_last, null_address_first, -1):
        null_address[street_position] = 0 if street[street_position] == 0 else min(null_address[street_position], null_address[street_position+1] + 1)

    for street_position in range(null_address_first-1, -1, -1):
        null_address[street_position] = null_address[street_position+1] + 1

    return null_address


n = int(input())
street = list(map(int, input().split()))
if __name__ == "__main__":
    print(nearest_null(n, street)))



ID  54682362
https://contest.yandex.ru/contest/23390/run-report/54682362/

from collections import Counter


def game(hands, data):

    counter = Counter([int(x) for x in data])
    score = 0
    for iteration in range(0, 10):
        if (iteration in counter) and (counter[iteration] <= hands*2):
            score += 1
    return score


hands = int(input())
data = list((''.join([input() for i in range(4)])).replace('.', ''))
if __name__ == "__main__":
    print(game(hands, data))
