def GetHash(item, start, finish):
    hash = 0
    base = 1000
    mod = 1000009
    print(f'GetHash start                        {start}')
    print(f'GetHash finish                       {finish}')
    hash = int(item) * int(base) % int(mod)
    print(f'GetHash hash                         {hash}')
    return hash


def GetHashes(items):
    hashes = []
    hash = 0
    base = 1000
    mod = 1000009
    for i in range(len(items)):
        print(f'GetHashes i                            {i}')
        print(f'GetHashes len(items)                   {len(items)}')
        print(f'GetHashes items[i]                     {items[i]}')
        hash = int(items[i] * int(base)) % int(mod)
        print(f'GetHashes hash {hash}')
        hashes.append(hash)
        print(f'GetHashes hashes {hashes}')
    return hashes


def CheckCollision(left_part_hash: str, right_part_hash: str, left: int, right: int, window: int):
    hashes = str()
    print(f'CheckCollision hashes before check          {hashes}')
    print(f'CheckCollision left_part_hash               {left_part_hash}')
    print(f'CheckCollision right_part_hash              {right_part_hash}')
    for i in range(left - 1, right, 1):
        print(f'CheckCollision i add                        {i}')
        hashes.__add__(str(left_part_hash[i]))
        print(f'CheckCollision left_part_hash[i]            {left_part_hash[i]}')

    for i in range(left - 1, right, 1):
        hashes = str()
        print(f'CheckCollision find    i                  {i}')
        print(f'CheckCollision find    left - 1           {left - 1}')
        print(f'CheckCollision find    right              {right}')
        print(f'CheckCollision find    right_part_hash[i] {right_part_hash[i]}')
        left_part_hash = str()
        j = left_part_hash.find(str(right_part_hash[i]), left - 1, right)
        if j >= 0:
            print(f'CheckCollision find    j                  {j}')
            print(f'CheckCollision find    hashes              True')
            return True
        print(f'CheckCollision find    hashes              False')
        print(f'CheckCollision find    j                  {j}')
    return False


def GetLCS(left_array, right_array):
    max_len = 0
    left = 1
    right = min(len(left_array), len(right_array))
    print(f'GetLCS  right = min(len(left_array), len(right_array)) {right}')
    left_part_hash = GetHashes(left_array)
    print(f'GetLCS    left_part_hash          {left_part_hash}')
    right_part_hash = GetHashes(right_array)
    print(f'GetLCS    right_part_hash        {right_part_hash}')
    while left <= right:
        middle = (left + right) // 2
        print(f'GetLCS    left                         {left}')
        print(f'GetLCS    right                        {right}')
        print(f'GetLCS    middle                       {middle}')
        if (CheckCollision(left_part_hash, right_part_hash, left, right, middle)):
            max_len += 1
            print(f'if GetLCS  CheckCollision    max_len           {max_len}')
            left = middle + 1
            print(f'if GetLCS  CheckCollision    left = middle + 1 {left}')
        else:
            right = middle - 1
            print(f'if GetLCS  CheckCollision    right = middle - 1 {right}') 
    return max_len 


if __name__ == '__main__':
    M = int(input())
    left_array = [] * M
    left_array = input().split()
    N = int(input())
    right_array = [] * N
    right_array = input().split()
    res = GetLCS(left_array, right_array)
    print(f'res {res}')

