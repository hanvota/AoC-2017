# Advent of Code 2017, Day-06
# https://adventofcode.com/2017

def distribute(banks: list, length: int) -> list:
    largest = max(banks)
    index = banks.index(largest)
    banks[index] = 0
    for i in range(largest):
        banks[(index + i + 1) % length] += 1  # next location, wrap around based on length of list
    return banks


def solve(banks: str, part2=False) -> int:
    seen = 0  # number of  time that we see a repeat. If we see the same again, then return
    banks = list(map(int, banks.split('\t')))
    states = [banks]  # states seen
    count = 1
    length = len(banks)
    print(f'{banks}')
    while True:
        new_banks = distribute(banks.copy(), length)
        # print(new_banks)
        if new_banks in states:  # seen this state already
            if not part2:
                return count
            seen += 1
            if seen == 2:
                return count
            count = 0
            states = [new_banks]
        else:
            states.append(new_banks)
        banks = new_banks
        count += 1


def main():
    with open('Day-06-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip()

    print(f'Day 06, Part 1--Redistribution cycles = {solve(input_data, False)}')
    print(f'Day 06, Part 2--Redistribution cycles = {solve(input_data, True)}')


if __name__ == '__main__':
    main()
