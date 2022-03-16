def gen_binary(count, prefix, left=0, right=0):
    if left == count and right == count:
        print(prefix)
    else:
        if left < count:
            gen_binary(count, prefix + '(', left+1, right)
        if right < left:
            gen_binary(count, prefix + ')', left, right+1)


def main():
    var_qty = int(input())
    prefix = ''
    gen_binary(var_qty, prefix, left=0, right=0)


if __name__ == '__main__':
    main()
