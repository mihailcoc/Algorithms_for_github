import heapq
import logging
from time import perf_counter

logging.basicConfig(filename='logging_heap.log', filemode='w', level=logging.DEBUG)


class Document:
    def __init__(self, doc_id, relevance):
        self.doc_id = doc_id
        self.relevance = relevance

    def __lt__(self, other):
        return self.relevance < other.relevance and self.doc_id < other.doc_id


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
                leftindex += 1
            else:
                result.append(right[rightindex])
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
    merged = merge(left, right)
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
    merged = merge_reverse(left, right)
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

        # Выполняем сравнения и сливаем части в соответствии со значениями элементов.
        # Добавляем условие > 1 чтобы убрать из сортировки большую часть элементов.
        if left[leftindex][1] > right[rightindex][1] and (left[leftindex][1] > 1 or right[rightindex][1] > 1):
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1

        # Если левая или правая часть длиннее, добавляем
        # оставшиеся элементы к результату.
        if leftindex == len(left) or rightindex == len(right):
            result.extend(left[leftindex:]
            or right[rightindex:])
            break

    return result


def prepare_index(size: int) -> list:
    size = int(infile.readline())
    index = {}
    for i in range(size):
        #  print(f'prepare_index i {i}')
        doc_index = {}
        doc = infile.readline().split()
        doc = [word for word in doc]
        for word in doc:
            #  print(f'prepare_index len {len(doc)}')
            #  print(f'prepare_index word {word}')
            #  print(f'prepare_index doc {doc}')
            if word in doc_index:
                doc_index[word] += 1
            else:
                doc_index[word] = 1
            #  print(f'prepare_index doc_index[word] = 1 {word}')
            #  print(f'prepare_index index {doc_index}')
        index.__setitem__(i, doc_index)
        #  print(f'prepare_index index {doc_index}')
        #  print(f'prepare_index index {index}')
    return size, index


def prepare_hash_dict(size: int, index) -> list:
    hash_dict = {}
    line = index.items()
    for doc_id in range(size):
        #  print(f'prepare_hash_dict doc_id {doc_id}')
        line = index[doc_id]
        #  print(f'prepare_hash_dict line {line}')
        for hash_word in line.keys():
            #  print(f'for hash word in line keys hash_word {hash_word}')
            if hash_word not in hash_dict.keys():
                #  print(f'if prepare_hash_dict hash_word {hash_word}')
                hash_rating_in_line = index[doc_id][hash_word]
                hash_word_dict = {}
                #  print(f'if prepare_hash_dict hash_word_dict {hash_word_dict}')
                hash_word_dict.__setitem__(doc_id + 1, hash_rating_in_line)
                #  print(f'if prepare_hash_dict hash_word_dict line_number {line_number}')
                #  print(f'if prepare_hash_dict hash_word_dict hash_rating_in_line {hash_rating_in_line}')
                hash_dict.__setitem__(hash_word, hash_word_dict)
                #  print(f'if prepare_hash_dict hash_dict {hash_dict}')
            else:
                #  print(f'else is hash word in dict hash_word {hash_word}')
                hash_rating_in_line = index[doc_id][hash_word]
                #  print(f'else is hash word in dict hash_rating_in_line {hash_rating_in_line}')
                hash_word_dict_two = {}
                hash_word_dict_two.__setitem__(doc_id + 1, hash_rating_in_line)
                hash_word_dict = hash_dict[hash_word]
                hash_word_dict.update(hash_word_dict_two)
                #  print(f'else is hash word in dict prepare_hash_dict hash_word_dict {hash_word_dict}')
                hash_dict.__setitem__(hash_word, hash_word_dict)
                #  print(f'else is hash word in dict prepare_hash_dict hash_dict {hash_dict}')
    return hash_dict


def calc_relevance(hash_dict: list, query: str) -> list:
    #  print(f'calc_relevance hash_dict {hash_dict}')
    ranked_index = {}
    ranked_index_list = []
    query_unique = {word for word in query.split()}
    #  hash_dict_list = list(hash_dict.items())
    #  for hash_word in hash_dict.keys():
    #  print(f'calc_relevance hash_word in hash_dict {hash_word}')
    for word in query_unique:
        #  print(f'calc_relevance word in query {word}')
        #  print(f'calc_relevance hash_dict {hash_dict}')
        # hash_word = binarySearch(hash_dict, word)
        #  print(f'calc_relevance hash_word {hash_word}')
        if word in hash_dict:
            hash_word_dict = hash_dict[word]
            #  print(f'calc_relevance hash_word_dict {hash_word_dict}')
            for doc_id in hash_word_dict.keys():
                rank = 0
                #  print(f'calc_relevance doc_id  {doc_id}')
                if doc_id in ranked_index:
                    rank = 0
                    word_value_in_string = hash_word_dict[doc_id]
                    word_value_in_ranked_index = ranked_index[doc_id]
                    #  print(f'calc_relevance if doc_id in ranked_index    word_value_in_string {word_value_in_string}')
                    #  print(f'calc_relevance if doc_id in ranked_index    word_value_in_ranked_index {word_value_in_ranked_index}')
                    rank = word_value_in_string + word_value_in_ranked_index
                    #  print(f'calc_relevance if doc_id in ranked_index    rank {rank}')
                    ranked_index[doc_id] = rank
                    #  print(f'calc_relevance ranked_index {ranked_index}')
                    #  ranked_index.update({doc_id: rank})
                else:
                    rank = 0
                    rank = hash_word_dict[doc_id]
                    #  print(f'calc_relevance else doc_id in ranked_index    rank {rank}')
                    #  ranked_index.update({doc_id: rank})
                    ranked_index[doc_id] = rank
                    #  print(f'calc_relevance ranked_index {ranked_index}')
            ranked_index_list = list(ranked_index.items())
    return ranked_index_list


if __name__ == '__main__':
    test_no = '26'
    input_file = f'test_data/{test_no}.input'
    output_file = f'test_data/{test_no}.output'
    open(output_file, 'w').close()
    t_begin = perf_counter()
    with open(input_file, 'r') as infile:
        size, index = prepare_index(infile)
        hash_dict = prepare_hash_dict(size, index)
        hash_dict_sorted_tuple = sorted(hash_dict.items(), key=lambda x: x[0])
        hash_dict = dict(hash_dict_sorted_tuple)
        #  hash_dict = merge_sort(hash_dict)
        query_count = int(infile.readline())
        for _ in range(query_count):
            query = infile.readline()
            relevant_docs = calc_relevance(hash_dict, query)
            relevant_docs = merge_sort_reverse(relevant_docs)
            #  print(f'main merge_sort_reverse relevant_docs {relevant_docs}')
            relevant_docs = merge_sort(relevant_docs)
            #  print(f'main merge_sort relevant_docs{relevant_docs}')
            relevant_docs = [item[0] for item in relevant_docs[:5]]
            #  print(f'main ranked_index_list{relevant_docs}')
            # relevant_docs.sort(key=lambda doc: doc[1], reverse=True)
            print(*relevant_docs)
        logging.debug(f'Calculations took {perf_counter() - t_begin} seconds')
            

    # testing output against the answer
    f1 = open(output_file, 'r')
    f2 = open(f'test_data/{test_no}.answer', "r")

    i = 0

    for line1 in f1:
        i += 1

        for line2 in f2:

            # matching line1 from both files
            if line1 == line2:
                # print IDENTICAL if similar
                print("Line ", i, ": IDENTICAL")
            else:
                print("Line ", i, ":")
                # else print that line from both files
                print("\tOutput:", line1, end='')
                print("\tAnswer:", line2, end='')
            break

    # closing files
    f1.close()
    f2.close()