def effective_solution(A, x, n):
    history = set()
    x.sort()
    triples = set()
    for i in range(n):
        for j in range(i + 1, n):
            for h in range(j + 1, n):
                for k in range(h + 1, n):
                    target = A - int(x[i]) - int(x[j]) - int(x[h]) - int(x[k])
                    if target in history:
                    # Заметим, что тут тройка уже отсортирована за счёт предварительной
                    # сортировки всего массива.
                        triples.add((target, x[i], x[j], x[h], x[k]))
                    history.add(x[i])
    return triples


if __name__ == '__main__':
    N = int(input())
    A = int(input())
    x = []
    x = input().split()
    print(effective_solution(A, x, N), sep='\n')

