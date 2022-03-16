def GetHash(string: str, q: int, r: int) -> int:
    if len(string) == 0:
        return 0
    poly_hash = ord(string[0]) % r
    for i in range(1, len(string)):
        poly_hash = (poly_hash * q + ord(string[i])) % r
    return poly_hash


def CheckCollision(lhs, rhs, window: int) -> bool:
    hashes = set()
    for start in range(M-window+1):
        substring_hash = GetHash(''.join(lhs[start:start+window]),
                                          539, 2147483648)
        hashes.add(substring_hash)
    for start in range(N-window+1):
        substring_hash = GetHash(''.join(rhs[start:start+window]),
                                          539, 2147483648)
        if substring_hash in hashes:
            return True
    return False


def GetLCS(lhs, rhs) -> int:
    size = 0
    left = 1
    right = min(M, N)
    while left <= right:
        mid = (left + right) // 2
        if CheckCollision(lhs, rhs, mid):
            size = mid
            left = mid + 1
        else:
            right = mid - 1
    return size


if __name__ == '__main__':
    M = int(input())
    left_array = input().split()
    N = int(input())
    right_array = input().split()
    print(GetLCS(left_array, right_array))