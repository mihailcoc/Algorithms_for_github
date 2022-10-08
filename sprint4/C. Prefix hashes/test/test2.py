import logging
import string
from time import perf_counter
from guppy import hpy

logging.basicConfig(filename='logging_v1.log', filemode='w', level=logging.DEBUG)


def my_hash(i):
    return (hashes[i - 1] * a % m + ord(s[i])) % m


def get_hash_substring(l, r):
    return (hashes[r] - hashes[l - 1] * pow(a, r - l + 1, m)) % m


if __name__ == '__main__':
    # start mem snapshot
    hp = hpy()
    before = hp.heap()

    with open('test_data/11 (13).txt', 'r') as infile:
        # initial input
        a = int(infile.readline())
        m = int(infile.readline())
        s = infile.readline()
        n = int(infile.readline())
        hashes = [0] * (len(s) + 1)

        logging.debug('Pre-calculating hashes...')
        t_start = perf_counter()
        for i in range(len(s)):
            hashes[i] = my_hash(i)
        logging.debug(f'Hashes pre-calculated in {perf_counter() - t_start} seconds.')

        logging.debug('Running main loop...')
        t_start = perf_counter()
        for _ in range(n):
            l, r = infile.readline().split()
            print(get_hash_substring(int(l) - 1, int(r) - 1))
        logging.debug(f'Main loop done in {perf_counter() - t_start} seconds.')

        after = hp.heap()
        logging.debug(f'{after - before}')