if __name__ == '__main__':
    # input
    Q = int(input())
    R = int(input())
    s = input()
    s_len = len(s)
    n = int(input())

    # cals powers of Q
    powers = [1]* (s_len)
    for i in range(1, s_len):
        powers[i] = (powers[i - 1] * Q) % R

    # calc hashes of prefixes
    hashes = [0]* (s_len + 1)
    for i in range(s_len):
        hashes[i] = (hashes[i-1] * Q + ord(s[i])) % R

    for _ in range(n):
        l, r = input().split()
        l, r = int(l)-1, int(r)-1
        print((hashes[r] - hashes[l - 1] * powers[r - l + 1]) % R)