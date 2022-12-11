# Advent of Code 2017, Day-02
# https://adventofcode.com/2017
from itertools import permutations


def checksum_1(data: list) -> int:
    total = 0
    for input_line in data:
        line = list(map(int, input_line.split('\t')))
        minimum = min(line)
        maximum = max(line)
        total += maximum - minimum
    return total


def divisible(n1: int, n2: int) -> int:
    if n1 % n2 == 0:
        return n1 // n2
    else:
        return 0


def checksum_2(data: list) -> int:
    total = 0
    for input_line in data:
        line = list(map(int, input_line.split('\t')))
        for perm in permutations(line, 2):
            n1, n2 = perm
            total += divisible(n1, n2)
    return total


def main():
    with open('Day-02-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip().split('\n')

    print(f'Day 02, Part 1--Checksum is {checksum_1(input_data)}')
    print(f'Day 02, Part 1--Checksum is {checksum_2(input_data)}')


if __name__ == '__main__':
    main()
