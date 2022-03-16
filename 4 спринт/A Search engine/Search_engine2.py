import hashlib


def GetHash(item):
    bytes_str = item.encode()
    return hashlib.shake_256(bytes_str).hexdigest(15)


def prepare_index(size: int) -> list:
    index = []
    for i in range(size):
        doc_index = {}
        doc = input().split()
        for word in doc:
            word = GetHash(word)
            if word in doc_index:
                doc_index[word] += 1
            else:
                doc_index[word] = 1
        index.append(doc_index)
    return index


def calc_relevance(index: list, query: str) -> list:
    ranked_index = []
    query_unique = {GetHash(word) for word in query.split()}

    #  print(f'calc_relevance query_unique {query_unique}')
    for doc_id, doc in enumerate(index):
        rank = 0
        for word in query_unique:
            word_value = doc.get(word)
            rank += word_value if word_value is not None else 0
        if rank:
            ranked_index.append((doc_id+1, rank))
    return ranked_index


if __name__ == '__main__':
    documents_count = int(input())
    index = prepare_index(documents_count)
    query_count = int(input())
    for _ in range(query_count):
        query = input()
        relevant_docs = calc_relevance(index, query)
        relevant_docs.sort(key=lambda doc: doc[1], reverse=True)
        print(*[item[0] for item in relevant_docs[:5]])
