def my_hash(i):
    return (hashes[i - 1] * a % m + ord(s[i])) % m


def get_hash_substrings(left, right):
    return (hashes[right] - hashes[left - 1] * pow(a, right - left + 1, m)) % m


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()
    hashes = [0] * (len(s) + 1)
    for i in range(len(s)):
        hashes[i] = my_hash(i)
    for _ in range(int(input())):
        l, r = input().split()
        result = get_hash_substrings(int(l) - 1, int(r) - 1)
        print(result, sep='\n')
