import heapq


class Document:
    def __init__(self, doc_id, relevance):
        self.doc_id = doc_id
        self.relevance = relevance

    def __lt__(self, other):
        return self.relevance < other.relevance and self.doc_id < other.doc_id


def prepare_index(infile) -> list:
    documents_count = int(infile.readline())
    index = []
    for i in range(documents_count):
        doc_index = {}
        doc = infile.readline().split()
        for word in doc:
            if word in doc_index:
                doc_index[word] += 1
            else:
                doc_index[word] = 1
        index.append(doc_index)
    return index


def calc_relevance(index: list, query: str) -> list:
    ranked_index = []
    query_unique = {word for word in query.split()}
    for doc_id, doc in enumerate(index):
        rank = 0
        for word in query_unique:
            word_value = doc.get(word)
            rank += word_value if word_value is not None else 0
        if rank:
            heapq.heappush(ranked_index, Document(doc_id=doc_id+1, relevance=rank))
    return heapq.nlargest(5, ranked_index, key=lambda doc: doc.relevance)


if __name__ == '__main__':
    test_no = '07'
    input_file = f'test_data/{test_no}.input'
    output_file = f'test_data/{test_no}.output'
    open(output_file, 'w').close()
    with open(input_file, 'r') as infile:
        index = prepare_index(infile)
        query_count = int(infile.readline())
        for _ in range(query_count):
            query = infile.readline()
            relevant_docs = calc_relevance(index, query)
            # relevant_docs.sort(key=lambda doc: doc[1], reverse=True)
            # print(*[item[0] for item in relevant_docs[:5]])
            with open(output_file, 'a') as outfile:
                # print(*[item[0] for item in relevant_docs[:5]], file=outfile)
                for item in relevant_docs:
                    outfile.write(f'{item.doc_id} ')
                outfile.write(f'\n')

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
