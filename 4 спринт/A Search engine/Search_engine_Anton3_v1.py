def prepare_index_2(size: int) -> dict:
    index = dict()
    for doc_id in range(size):
        doc = [word for word in input().split()]
        for word in doc:
            word_dict = index.get(word)
            word_cnt = {doc_id+1: doc.count(word)}
            if word_dict:
                word_dict.update(word_cnt)
            else:
                index[word] = word_cnt
    return index


def calc_relevance_2(index: dict, query: str) -> dict:
    query_unique = {word for word in query.split()}
    ranked_index = dict()
    for word in query_unique:
        word_docs_index = index.get(word)
        if word_docs_index is None:
            continue
        ranked_index = {
            k: ranked_index.get(k, 0) + word_docs_index.get(k, 0)
            for k in set(ranked_index) | set(word_docs_index)}
    return ranked_index


if __name__ == '__main__':
    size = int(input())
    index = prepare_index_2(size)
    query_count = int(input())
    for _ in range(query_count):
        query = input()
        relevant_docs = calc_relevance_2(index, query)
        relevant_docs = sorted(relevant_docs.items(), key=lambda x: x[1], reverse=True)
        relevant_docs.sort(key=lambda x: (-x[1], x[0]), reverse=False)
        print(*[item[0] for item in relevant_docs[:5]])
