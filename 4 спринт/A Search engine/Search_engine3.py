import hashlib


def GetHash(item):
    bytes_str = item.encode()
    return hashlib.shake_256(bytes_str).hexdigest(15)


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
    index = {}
    for i in range(size):
        #  print(f'prepare_index i {i}')
        doc_index = {}
        doc = [GetHash(word) for word in input().split()]
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
    return index


def calc_relevance(index: list, query: str) -> list:
    ranked_index = []
    ranked_index_temp = []
    for doc_id in index.keys():
        rank = 0
        for word in query:
            if word in index[doc_id]:
                word_value = index[doc_id][word]
                rank += word_value if word_value is not None else 0
        if rank:
            ranked_index_temp.append((doc_id+1, rank))
    ranked_index_temp = merge_sort_reverse(ranked_index_temp)
    ranked_index_temp = merge_sort(ranked_index_temp)
    ranked_index = [item[0] for item in ranked_index_temp[:5]]
    return ranked_index


if __name__ == '__main__':
    documents_count = int(input())
    index = prepare_index(documents_count)
    #  print(f'name prepare_index  {index}')
    query_count = int(input())
    for _ in range(query_count):
        query = {GetHash(word) for word in input().split()}
        relevant_docs = calc_relevance(index, query)
        #  relevant_docs1 = merge_sort_reverse(relevant_docs)
        #  relevant_docs2 = merge_sort(relevant_docs1)
        #  print(f'name relevant_docs  {relevant_docs}')
        #  relevant_docs.sort(key=lambda doc: doc[1], reverse=True)
        #  print(*[item[0] for item in relevant_docs2[:5]])
        print(*relevant_docs)