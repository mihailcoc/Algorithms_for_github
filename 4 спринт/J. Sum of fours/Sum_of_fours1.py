def naive_solution(A, x, n):
    triples = []
    n = len(x)
    x.sort()
    for i1 in range(n):
        print(f' iteration1 "{x[i1]}" ')
        for i2 in range(i1 + 1, n):
            print(f' iteration2 "{x[i2]}" ')
            for i3 in range(i2 + 1, n):
                print(f' iteration3 "{x[i3]}" ')
                for i4 in range(i3 + 1, n):
                    print(f' iteration4 summ "{(int(x[i1]) + int(x[i2]) + int(x[i3]) + int(x[i4]))}" ')
                    print(f' A "{A}" ')
                    if (int(x[i1]) + int(x[i2]) + int(x[i3]) + int(x[i4])) == A:
                        print(f' x[i1] "{x[i1]}" ')
                        print(f' x[i2] "{x[i2]}" ')
                        print(f' x[i3] "{x[i3]}" ')
                        print(f' x[i4] "{x[i4]}" ')
                        triples.append(sorted((x[i1], x[i2], x[i3], x[i4])))
                        print(f' triples "{triples}" ')
    return triples


if __name__ == '__main__':
    N = int(input())
    A = int(input())
    x = []
    x = input().split()
    print(x)
    result = (naive_solution(A, x, N))
    print(result, sep='\n')
