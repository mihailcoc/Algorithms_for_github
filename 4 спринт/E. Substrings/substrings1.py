def longest_substring(string: str) -> int:
    result = 0
    last_pos = 0
    char_position = [0] * 26
    for i in range(len(string)):
        rel_index = ord(string[i])-97
        last_pos = max(last_pos, char_position[rel_index])
        char_position[rel_index] = i+1
        result = max(result, i - last_pos + 1)
    return result


if __name__ == '__main__':
    print(longest_substring(input()))