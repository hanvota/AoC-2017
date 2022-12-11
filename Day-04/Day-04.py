# Advent of Code 2017, Day-04
# https://adventofcode.com/2017

from itertools import permutations


def passphrase_1(data: list) -> int:
    count = 0
    for input_line in data:
        line_list = input_line.split(' ')
        line_set = set(line_list)
        if len(line_list) == len(line_set):
            count += 1

    return count


def is_anagram(word1: str, word2: str) -> bool:
    word1_list = list(word1)
    word2_list = list(word2)
    for letter in word1_list:
        if letter in word2_list:
            word2_list.remove(letter)
    if len(word2_list) == 0:
        return True
    else:
        return False


def passphrase_2(data: list) -> int:
    count = 0
    for input_line in data:
        line_list = input_line.split(' ')
        perm = permutations(line_list, 2)
        for word_pair in perm:
            word1, word2 = word_pair
            if len(word1) != len(word2):
                continue
            if is_anagram(word1, word2):
                break
        else:
            count += 1

    return count


def main():
    with open('Day-04-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip().split('\n')

    print(f'Day 04, Part 1--Number of valid passphrases is {passphrase_1(input_data)}')
    print(f'Day 04, Part 2--Number of valid passphrases is {passphrase_2(input_data)}')


if __name__ == '__main__':
    main()
