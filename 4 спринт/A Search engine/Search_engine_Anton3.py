import logging
from time import perf_counter

logging.basicConfig(filename='logging_heap.log', filemode='w', level=logging.DEBUG)


def prepare_index_2(infile) -> dict:
    documents_count = int(infile.readline())
    index = dict()
    for doc_id in range(documents_count):
        doc = infile.readline().split()
        for word in doc:
            word_dict = index.get(word)
            word_cnt = {doc_id+1: doc.count(word)}
            if word_dict:
                word_dict.update(word_cnt)
            else:
                index[word] = word_cnt
    return index


def calc_relevance_2(index: dict, query: str):
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
    test_no = '26'
    input_file = f'test_data/{test_no}.input'
    output_file = f'test_data/{test_no}.output'
    open(output_file, 'w').close()
    t_begin = perf_counter()
    with open(input_file, 'r') as infile:
        index_begin = perf_counter()
        index = prepare_index_2(infile)
        logging.debug(f'index prepared in {perf_counter() - index_begin} seconds')
        query_count = int(infile.readline())
        for _ in range(query_count):
            query = infile.readline()
            calc_rel_begin = perf_counter()
            relevant_docs = calc_relevance_2(index, query)
            logging.debug(f'calc_relevance (total) in {perf_counter() - calc_rel_begin} seconds')
            relevant_docs = sorted(relevant_docs.items(), key=lambda x: (x[1], -x[0]), reverse=True)
            with open(output_file, 'a') as outfile:
                for item in relevant_docs[:5]:
                    outfile.write(f'{item[0]} ')
                outfile.write(f'\n')
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
