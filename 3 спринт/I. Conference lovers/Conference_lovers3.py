def main():
    _ = int(input())
    id_count = dict()
    ids = input().split()
    for next_id in ids:
        if next_id in id_count:
            id_count[next_id] += 1
        else:
            id_count[next_id] = 1
    k = int(input())
    id_count = sorted(id_count.items(), key=lambda item: item[1], reverse=True)
    for key, _ in id_count[:k]:
        print(key, end=' ')


if __name__ == '__main__':
    main()