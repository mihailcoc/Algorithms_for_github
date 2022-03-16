def get_hashes_of_slice(base, mod, prefix_hashes, bases, start, end):
    if start == 0:
        print(prefix_hashes[end])
        return

    previous_part_hash = prefix_hashes[start-1]
    to_end_hash = prefix_hashes[end]

    power = end - start + 1

    powered_base = get_powered_base(bases, base, power)

    print((to_end_hash - previous_part_hash * powered_base) % mod)


def get_prefix_hashes(base, mod, string):
    length = len(string)
    hashes = [0] * length
    i = 0

    hashs_sum = 0
    while i < length:
        chr_val = ord(string[i])
        hashes[i] = hashs_sum + (chr_val % mod)
        hashs_sum = ((hashs_sum + chr_val) * base) % mod
        i += 1

    return hashes