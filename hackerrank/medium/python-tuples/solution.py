def old_tuple_hash(t):
    mask = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    length = len(t)
    for item in t:
        length -= 1
        x = ((x ^ hash(item)) * mult) & mask
        mult = (mult + 82520 + length + length) & mask
    x = (x + 97531) & mask
    if x >= 1 << 63:
        x -= 1 << 64
    if x == -1:
        x = -2
    return x

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(old_tuple_hash(t))
