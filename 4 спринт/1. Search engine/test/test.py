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
        # кол-во подстрок для обработки
        size = int(infile.readline())
        print(f'prepare_index size {size}')
        # calc prepare_index
        t_begin = perf_counter()
        index = []
        for i in range(size):
            #  print(f'prepare_index i {i}')
            doc_index = {}
            doc = infile.readline().split()
            # print(f'prepare_index doc {doc}')
            for word in doc:
                #  print(f'prepare_index word {word}')
                if word in doc_index:
                    doc_index[word] += 1
                else:
                    doc_index[word] = 1
            index.append(doc_index)
            #  print(f'prepare_index index {index}')
        #  print(f'prepare_index index {index}')
        logging.debug(f'Prepare_index of {size} calculated in {perf_counter()-t_begin} seconds')

        # calc_relevance
        t_begin = perf_counter()
        query_count = int(infile.readline())
        # print(f'calc_relevance query_count {query_count}')
        for _ in range(query_count):
            query = infile.readline()
            #  print(f'calc_relevance query {query}')
            ranked_index = []
            #  print(f'calc_relevance ranked_index {ranked_index}')
            query_unique = {word for word in query.split()}

            #  print(f'calc_relevance query_unique {query_unique}')
            for doc_id, doc in enumerate(index):
                #  print(f'calc_relevance doc_id {doc_id}')
                #  print(f'calc_relevance doc {doc}')
                rank = 0
                for word in query_unique:
                    #  print(f'calc_relevance word {word}')
                    word_value = doc.get(word)
                    #  print(f'calc_relevance word_value {word_value}')
                    rank += word_value if word_value is not None else 0
                    #  print(f'calc_relevance rank {rank}')
                if rank:
                    ranked_index.append((doc_id+1, rank))
                    #  print(f'calc_relevance ranked_index {ranked_index}')
            #  print(f'calc_relevance ranked_index {ranked_index}')
        logging.debug(f'Calc_relevance calculated in {perf_counter()-t_begin} seconds')

        after = hp.heap()
        logging.debug(f'{after - before}')


if __name__ == '__main__':
    # main('test_data/07.input')
    main('test_data/15.input')
