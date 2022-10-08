import logging
import random
import string
import sys
import guppy
from time import perf_counter
from guppy import hpy
import hashlib



def GetHash(item):
    bytes_str = item.encode()
    return hashlib.shake_256(bytes_str).hexdigest(15)


logging.basicConfig(filename='logging.log', filemode='w', level=logging.DEBUG)


def gen_string(size: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=size))


def merge(left, right):
    # Если левая или правая часть пуста, мы имеем дело список
    # единственной частью, которая уже отсортирована.
    if not len(left):
        return left
    if not len(right):
        return right

    # Определение переменных для процесса слияния.
    result = []
    leftindex = 0
    rightindex = 0
    totalLen = len(left) + len(right)

    # Работаем, пока не будут объединены все элементы.
    while (len(result) < totalLen):

        # Выполняем сравнения и сливаем части
        # в соответствии со значениями элементов.
        if left[leftindex][1] > right[rightindex][1]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            if left[leftindex] < right[rightindex]:
                result.append(left[leftindex])
                #  print(f'merge left[leftindex]  {left[leftindex]}')
                #  print(f'merge right[rightindex]  {right[rightindex]}')
                #  print(f'merge result.append(left[leftindex])  {result}')
                leftindex += 1
            else:
                result.append(right[rightindex])
                #  print(f'merge left[leftindex]  {left[leftindex]}')
                #  print(f'merge right[rightindex]  {right[rightindex]}')
                #  print(f'merge result.append(right[rightindex])  {result}')
                rightindex += 1
        # Если левая или правая часть длиннее, добавляем
        # оставшиеся элементы к результату.
        if leftindex == len(left) or rightindex == len(right):
            result.extend(left[leftindex:]
            or right[rightindex:])
            break

    return result


def merge_sort(list):
    # Проверяем разбит ли список на отдельные части.
    if len(list) < 2:
        return list
    # Находим средину списка.
    middle = len(list)//2

    # Разбиваем список на две части.
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])

    # Объединяем отсортированные части в одну.
    #  print("Левая часть:", left)
    #  print("Правая часть:", right)
    merged = merge(left, right)
    #  print("Объединены в ", merged)
    return merged


def merge_sort_reverse(list):
    # Проверяем разбит ли список на отдельные части.
    if len(list) < 2:
        return list
    # Находим средину списка.
    middle = len(list)//2

    # Разбиваем список на две части.
    left = merge_sort_reverse(list[:middle])
    right = merge_sort_reverse(list[middle:])

    # Объединяем отсортированные части в одну.
    #  print("Левая часть:", left)
    #  print("Правая часть:", right)
    merged = merge_reverse(left, right)
    #  print("Объединены в ", merged)
    return merged


def merge_reverse(left, right):
    # Если левая или правая часть пуста, мы имеем дело список
    # единственной частью, которая уже отсортирована.
    if not len(left):
        return left
    if not len(right):
        return right

    # Определение переменных для процесса слияния.
    result = []
    leftindex = 0
    rightindex = 0
    totalLen = len(left) + len(right)

    # Работаем, пока не будут объединены все элементы.
    while (len(result) < totalLen):

        # Выполняем сравнения и сливаем части
        # в соответствии со значениями элементов.
        if left[leftindex][1] > right[rightindex][1] and (left[leftindex][1] > 1 or right[rightindex][1] > 1):
            result.append(left[leftindex])
            #  print(f'merge_reverse left[leftindex][1]  {left[leftindex][1]}')
            #  print(f'merge_reverse right[rightindex][1]  {right[rightindex][1]}')
            #  print(f'merge_reverse result.append(left[leftindex])  {result}')
            leftindex += 1
        else:
            result.append(right[rightindex])
            #  print(f'merge_reverse left[leftindex]  {left[leftindex][1]}')
            #  print(f'merge_reverse right[rightindex]  {right[rightindex][1]}')
            #  print(f'merge_reverse result.append(right[rightindex])  {result}')
            rightindex += 1

        # Если левая или правая часть длиннее, добавляем
        # оставшиеся элементы к результату.
        if leftindex == len(left) or rightindex == len(right):
            result.extend(left[leftindex:]
            or right[rightindex:])
            break

    return result


def calc_relevance(index: list, query: str) -> list:
    Calc_relevance_for_word_in_query_unigue = int()
    Calc_relevance_for_enumerate = int()
    Calc_relevance_relevant_docs_print = int()
    ranked_index = []
    #  print(f'calc_relevance ranked_index {ranked_index}')
    query_unique = {GetHash(word) for word in query.split()}

    #  print(f'calc_relevance query_unique {query_unique}')
    Calc_relevance_for_enumerate_t_begin = perf_counter()
    for doc_id, doc in enumerate(index):
        #  print(f'calc_relevance doc_id {doc_id}')
        #  print(f'calc_relevance doc {doc}')
        rank = 0
        for word in query_unique:
            Calc_relevance_for_word_in_query_unigue_t_begin = perf_counter()
            #  print(f'calc_relevance word {word}')
            word_value = doc.get(word)
            #  print(f'calc_relevance word_value {word_value}')
            rank += word_value if word_value is not None else 0
            #  print(f'calc_relevance rank {rank}')
            Calc_relevance_for_word_in_query_unigue = perf_counter() - Calc_relevance_for_word_in_query_unigue_t_begin
        if rank:
            Calc_relevance_if_rank_t_begin = perf_counter()
            ranked_index.append((doc_id+1, rank))
            Calc_relevance_if_rank = perf_counter() - Calc_relevance_if_rank_t_begin
            #  print(f'calc_relevance ranked_index {ranked_index}')
    #  print(f'calc_relevance ranked_index {ranked_index}')
    Calc_relevance_for_enumerate = perf_counter() - Calc_relevance_for_enumerate_t_begin
    return ranked_index, Calc_relevance_for_word_in_query_unigue, Calc_relevance_if_rank, Calc_relevance_for_enumerate


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
            for word in doc:
                #  print(f'prepare_index word {word}')
                word = GetHash(word)
                if word in doc_index:
                    doc_index[word] += 1
                else:
                    doc_index[word] = 1
            index.append(doc_index)
            #  print(f'prepare_index index {index}')
        #  print(f'prepare_index index {index}')
        logging.debug(f'Prepare_index of {size} calculated in {perf_counter()-t_begin} seconds')

        # calc_relevance
        #  Calc_relevance = int()
        main_merge_sort_reverse = int()
        main_merge_sort = int()
        relevant_docs_print = int()
        Calc_relevance_for_word_in_query_unigue_total = int()
        Calc_relevance_if_rank_total = int()
        Calc_relevance_for_enumerate_total = int()
        #  t_begin = perf_counter()
        query_count = int(infile.readline())
        print(f'calc_relevance query_count {query_count}')
        for _ in range(query_count):
            query = infile.readline()
            #  print(f'calc_relevance query {query}')
            t_begin = perf_counter()
            relevant_docs, Calc_relevance_for_word_in_query_unigue, Calc_relevance_if_rank, Calc_relevance_for_enumerate = calc_relevance(index, query)
            Calc_relevance_for_word_in_query_unigue_total = Calc_relevance_for_word_in_query_unigue_total + Calc_relevance_for_word_in_query_unigue
            Calc_relevance_if_rank_total = Calc_relevance_if_rank_total + Calc_relevance_if_rank
            Calc_relevance_for_enumerate_total = Calc_relevance_for_enumerate_total + Calc_relevance_for_enumerate
            Calc_relevance = perf_counter()-t_begin
            #  print(f'name relevant_docs  {relevant_docs}')
            t_begin = perf_counter()
            relevant_docs1 = merge_sort_reverse(relevant_docs)
            main_merge_sort_reverse = main_merge_sort_reverse + perf_counter()-t_begin
            t_begin = perf_counter()
            relevant_docs2 = merge_sort(relevant_docs1)
            main_merge_sort= main_merge_sort + perf_counter()-t_begin
            #  logging.debug(f'relevant_docs merge_sort calculated in {perf_counter()-t_begin} seconds')
            #  print(f'name relevant_docs.sort  {relevant_docs.sort(key=lambda doc: doc[1], reverse=True)}')
            t_begin = perf_counter()
            print(*[item[0] for item in relevant_docs2[:5]])
            relevant_docs_print = relevant_docs_print + perf_counter()-t_begin
            #  logging.debug(f'print calculated in {perf_counter()-t_begin} seconds')
        logging.debug(f'Calc_relevance calculated in {Calc_relevance} seconds') 
        logging.debug(f'Calc_relevance_for_word_in_query_unigue_total calculated in {Calc_relevance_for_word_in_query_unigue_total} seconds') 
        logging.debug(f'Calc_relevance_if_rank_total calculated in {Calc_relevance_if_rank_total} seconds')
        logging.debug(f'Calc_relevance_for_enumerate_total calculated in {Calc_relevance_for_enumerate_total} seconds')
        logging.debug(f'merge_sort_reverse calculated in {main_merge_sort_reverse} seconds')
        logging.debug(f'merge_sort calculated in {main_merge_sort} seconds')
        logging.debug(f'print calculated in {relevant_docs_print} seconds')

        after = hp.heap()
        logging.debug(f'{after - before}')


if __name__ == '__main__':
    #  main('test_data/07.input')
    main('test_data/15.input')