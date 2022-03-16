import logging
import random
import string
import sys
import guppy
from time import perf_counter
from guppy import hpy


logging.basicConfig(filename='logging.log', filemode='w', level=logging.DEBUG)


def gen_string(size: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=size))


def main(data: str):
    logging.debug(f'\nRunning tests from {data}...\n')

    # start mem snapshot
    hp = hpy()
    before = hp.heap()

    # initial input
    with open(data, 'r') as infile:
        # основание хеша [1 .. 1000]
        Q = int(infile.readline())

        # модуль хеша [1 .. 10^7]
        R = int(infile.readline())

        # строка
        s = infile.readline()

        # длина строки
        s_len = len(s)

        # кол-во подстрок для обработки
        n = int(infile.readline())

        # calc powers of Q
        t_begin = perf_counter()
        powers = [1] * (s_len+1)
        for i in range(1, s_len):
            powers[i] = (powers[i-1] * Q) % R
        logging.debug(f'Powers of {Q} calculated in {perf_counter()-t_begin} seconds')

        # calc hashes of prefixes
        t_begin = perf_counter()
        powers = [1] * (s_len+1)
        hashes = [0] * (s_len+1)
        for i in range(s_len):
            hashes[i] = (hashes[i-1] * Q + ord(s[i])) % R
        logging.debug(f'Hashes of prefixes calculated in {perf_counter()-t_begin} seconds')

        t_begin = perf_counter()
        with open('output.txt', 'w') as outfile:
            for _ in range(n):
                l, r = infile.readline().split()
                l, r = int(l)-1, int(r)-1

                # вычисление хеша подстроки за константу
                sub_hash = (hashes[r] - hashes[l-1] * powers[r-l+1]) % R
                outfile.write(f'{sub_hash}\n')
        logging.debug(f'Hashes of substrings calculated in {perf_counter() - t_begin} seconds\n')

        after = hp.heap()
        logging.debug(f'{after - before}')


if __name__ == '__main__':
    main('test_data/11 (13).txt')
    main('test_data/12 (14).txt')
    main('test_data/13 (15).txt')