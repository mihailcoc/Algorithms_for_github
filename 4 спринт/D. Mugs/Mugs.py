if __name__ == '__main__':
    N = int(input())
    all_circles = []
    for _ in range(N):
        new = input()
        if new in all_circles:
            pass
        else:
            all_circles.append(new)
    print(*all_circles, sep='\n')
