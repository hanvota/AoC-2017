# Advent of Code 2017, Day-10
# https://adventofcode.com/2017

# from collections import deque

CIRCLE_SIZE = 256
EXTRA_LENGTHS = [17, 31, 73, 47, 23]
ROUNDS_TO_RUN = 64
DENSE_HASH_SEG_SIZE = 16


def reverse_segment(circle: list, seg_length: int, curr: int) -> list:
    from_ = curr
    to_ = (from_ + seg_length - 1) % CIRCLE_SIZE
    for i in range(seg_length // 2):
        temp = circle[(from_ + i) % CIRCLE_SIZE]
        circle[(from_ + i) % CIRCLE_SIZE] = circle[(to_ - i) % CIRCLE_SIZE]
        circle[(to_ - i) % CIRCLE_SIZE] = temp
    return circle


def solve_1(data: str) -> int:
    circle = list(i for i in range(CIRCLE_SIZE))
    skip = 0
    curr = 0  # index of current position.
    seg_lengths = list(map(int, data.split(',')))
    seg_lengths.reverse()  # reverse in order to use list.pop
    while seg_lengths:
        segment_length = seg_lengths.pop()
        if segment_length > CIRCLE_SIZE:
            continue
        circle = reverse_segment(circle, segment_length, curr)
        curr = (curr + segment_length + skip) % CIRCLE_SIZE
        skip += 1

    return circle[0] * circle[1]


def generate_one_hash(circle, seg_lengths, curr, skip):
    for i in seg_lengths:
        circle = reverse_segment(circle, i, curr)
        curr = (curr + i + skip) % CIRCLE_SIZE
        skip += 1

    return curr, skip


def generate_dense_hash(circle, DENSE_HASH_SEG_SIZE):
    dense_hash = []

    for i in range(DENSE_HASH_SEG_SIZE):
        dense_hash_segment = circle[:DENSE_HASH_SEG_SIZE]
        circle = circle[DENSE_HASH_SEG_SIZE:]
        dh = 0
        for j in dense_hash_segment:
            dh = dh ^ j
        dense_hash.append(dh)
    return dense_hash


def generate_hex_string(dense_hash):
    hex_string = ''
    for i in dense_hash:
        hex_str = '0' + hex(i)[2:]  # exclude the '0x' and pad with leading '0'
        hex_str = hex_str[-2:]  # take the last 2 characters
        # print(hex_str)
        hex_string += hex_str

    return hex_string


def solve_2(data: str) -> str:
    circle = list(i for i in range(CIRCLE_SIZE))
    seg_lengths = list(ord(x) for x in data)
    seg_lengths.extend(EXTRA_LENGTHS)

    skip = 0
    curr = 0  # index of current position.
    # Generate sparce hash
    for _ in range(ROUNDS_TO_RUN):
        curr, skip = generate_one_hash(circle, seg_lengths, curr, skip)

    # circle now contains sparse hash, 256 number

    dense_hash = generate_dense_hash(circle, DENSE_HASH_SEG_SIZE)
    final_hex = generate_hex_string(dense_hash)

    return final_hex


def main():
    with open('Day-10-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip()

    print(f'Day 10, Part 1--Checksum (product of first two numbers) is: {solve_1(input_data)}')
    print(f'Day 10, Part 2--Knot Hash is: {solve_2(input_data)}')


if __name__ == '__main__':
    main()
