from collections import Counter


def game(hands, data):

    counter = Counter([int(x) for x in data])
    score = 0
    for iteration in range(0, 10):
        if (iteration in counter) and (counter[iteration] <= hands*2):
            score += 1
    return score


if __name__ == '__main__':
    hands = int(input())
    data = list((''.join([input() for i in range(4)])).replace('.', ''))
    print(game(hands, data))
