import logging
from time import perf_counter
from guppy import hpy

logging.basicConfig(filename='logging_v2.log', filemode='w', level=logging.DEBUG)


def my_hash(base, modulo, tring):
    if not tring:
        return 0
    tring[0] = tring[0] % modulo
    for num in range(1, len(tring)):
        tring[num] = (tring[num-1] * base + tring[num]) % modulo
    return tring


def exponential(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 0:
            exp = exp //2
            base = (base * base) % mod
        else:
            exp = exp -1
            result = result * base
            exp = exp //2
            base = (base * base) % mod
    return result % mod


if __name__ == '__main__':
    # start mem snapshot
    hp = hpy()
    before = hp.heap()

    with open('test_data/11 (13).txt', 'r') as infile:
        base = int(infile.readline())
        modulo = int(infile.readline())

        s = infile.readline()

        n = int(infile.readline())

        logging.debug('Hash pre-cal started...')
        t_start = perf_counter()
        new = my_hash(base, modulo, [ord(i) for i in s])
        logging.debug(f'Hash pre-calc done in {perf_counter() - t_start} seconds.')

        logging.debug('Main loop started...')
        t_start = perf_counter()
        for i in range(n):
            start, end = [int(i)-1 for i in infile.readline().split()]
            if start == 0:
                print(new[end])
            else:
                print((new[end]-new[start-1]*exponential(base, (end-start+1), modulo)) % modulo)
        logging.debug(f'Main loop done in {perf_counter() - t_start} seconds.')

        after = hp.heap()
        logging.debug(f'{after - before}')