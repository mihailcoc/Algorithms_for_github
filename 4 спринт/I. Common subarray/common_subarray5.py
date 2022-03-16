def poly_hash_gorner(string: str, q: int, r: int) -> int:
    if len(string) == 0:
        return 0
    poly_hash = ord(string[0]) % r
    print(f'poly_hash_gorner poly_hash          {poly_hash}')
    for i in range(1, len(string)):
        print(f'poly_hash_gorner i                  {i}')
        print(f'poly_hash_gorner poly_hash          {poly_hash}')
        poly_hash = (poly_hash * q + ord(string[i])) % r
    return poly_hash


def check_overlap(lhs, rhs, window: int) -> bool:
    hashes = set()
    print(f'check_overlap hashes                {hashes}')
    for start in range(len(lhs)-window+1):
        print(f'check_overlap start                {start}')
        substring_hash = poly_hash_gorner(''.join(lhs[start:start+window]),
                                          539, 2147483648)
        print(f'check_overlap substring_hash       {substring_hash}')
        hashes.add(substring_hash)
        print(f'check_overlap hashes               {hashes}')
    for start in range(len(rhs)-window+1):
        print(f'check_overlap start                {start}')
        substring_hash = poly_hash_gorner(''.join(rhs[start:start+window]),
                                          539, 2147483648)
        print(f'check_overlap substring_hash       {substring_hash}')
        if substring_hash in hashes:
            print(f'check_overlap    True           {True}')
            return True
    print(f'check_overlap    False           {False}')
    return False


def largest_common_subarray(lhs, rhs) -> int:
    size = 0
    left = 1
    right = min(len(lhs), len(rhs))
    print(f'largest_common_subarray right  {right}')
    while left <= right:
        mid = (left + right) // 2
        print(f'GetLCS    left                         {left}')
        print(f'GetLCS    right                        {right}')
        print(f'GetLCS    mid                          {mid}')
        if check_overlap(lhs, rhs, mid):
            size = mid
            print(f'if check_overlap    size           {size}')
            left = mid + 1
            print(f'if check_overlap    left           {left}')
        else:
            right = mid - 1
            print(f'if check_overlap    right          {right}')
    return size


if __name__ == '__main__':
    size_1 = int(input())
    results_1 = input().split()
    size_2 = int(input())
    results_2 = input().split()
    print(largest_common_subarray(results_1, results_2))