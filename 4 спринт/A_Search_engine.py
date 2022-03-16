#  https://contest.yandex.ru/contest/24414/run-report/63776373/

-- ПРИНЦИП РАБОТЫ --
Сначала алгоритм принимает базу из строк и создает из них словарь.
Ключи это номера строк а значение это словарь где ключ хеш от слова
а значение это частота с котрой слово встречается в строке.
Затем словарь конвертируется в словарь где ключами являются хеш
от слова, а значением словарь где ключ номер строки а значение это
частота, с которой слово встречается в тексте условия.
Затем словарь сортируется по ключам для быстрого поиска.
Потом для каждой строки из запроса определяется частота с которой
слово встречается  и результаты переносятся в массив.
В конце массив сортируется по релевантности и второй раз
сортируется по хэшам от слов и выводится на печать 
5 самых встречающихся слов из запроса.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания следует что после каждой итерации со словарём из условия
и словарем из запроса мы работаем с релевантностью.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность составления словаря O(N), потому что составление словаря
происходит путём прохода поочерёдно всех элементов массива из условия.
Поиск элементов в словаре происходит по отсортированным ключам,
поэтому поиск соответствия ключе в словаре и слов в запросе 
в среднем O(N/2).
В случае если запрос будет содержать все слова, но разном порядке,
то время поиска соответствия будет O(N/2), но будет зависеть от порядка
слов в запросе. Слова которые расположены ближе к началу словаря
будут находится быстрее, чем слова расположенные в конце словаря.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В пространственную сложность включается формирование двух словарей
из массива условия O(2n).

def prepare_index(size: int) -> dict:
    index = {}
    for i in range(size):
        doc_index = {}
        doc = [word for word in input().split()]
        for word in doc:
            if word in doc_index:
                doc_index[word] += 1
            else:
                doc_index[word] = 1
        index[i] = doc_index
    return size, index


def convert_to_word_dict(size: int, index: dict) -> dict:
    first_word_dict = {}
    line = index.items()
    for line_n in range(size):
        line = index[line_n]
        for word in line:
            if word not in first_word_dict:
                rating_in_line = index[line_n][word]
                second_word_dict = {}
                second_word_dict[line_n + 1] = rating_in_line
                first_word_dict[word] = second_word_dict
            else:
                rating_in_line = index[line_n][word]
                word_dict_from_index = {}
                word_dict_from_index[line_n + 1] = rating_in_line
                second_word_dict = first_word_dict[word]
                second_word_dict.update(word_dict_from_index)
                first_word_dict[word] = second_word_dict
    return first_word_dict


def calc_relevance(dictionary: dict, query: str) -> dict:
    ranked_index = {}
    query_unique = {word for word in query.split()}
    for word in query_unique:
        if word in dictionary:
            word_dict = dictionary[word]
            for line_n in word_dict:
                if line_n in ranked_index:
                    rank = 0
                    word_value_in_line = word_dict[line_n]
                    word_value_in_ranked_index = ranked_index[line_n]
                    rank = word_value_in_line + word_value_in_ranked_index
                    ranked_index[line_n] = rank
                else:
                    rank = 0
                    rank = word_dict[line_n]
                    ranked_index[line_n] = rank
    return ranked_index


if __name__ == '__main__':
    size = int(input())
    size, index = prepare_index(size)
    first_word_dict = convert_to_word_dict(size, index)
    word_dict_sorted = dict(sorted(first_word_dict.items(), key=lambda x: x[0]))
    query_count = int(input())
    for _ in range(query_count):
        query = input()
        relevant_docs = calc_relevance(word_dict_sorted, query)
        relevant_docs = sorted(relevant_docs.items(), key=lambda x: x[1], reverse=True)
        relevant_docs.sort(key=lambda x: (-x[1], x[0]), reverse=False)
        print(*[item[0] for item in relevant_docs[:5]])
