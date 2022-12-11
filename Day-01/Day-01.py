# Advent of Code 2017, Day-01
# https://adventofcode.com/2017


def solve_1(data: str) -> int:
    total = 0
    for curr_digit in range(len(data) - 1):
        if data[curr_digit] == data[curr_digit + 1]:
            total += int(data[curr_digit])
    if data[-1] == data[0]:
        total += int(data[-1])
    return total


def solve_2(data: str) -> int:
    total = 0
    data_length = len(data)
    for curr_digit in range(data_length):
        next_digit = (curr_digit + data_length // 2) % data_length
        if data[curr_digit] == data[next_digit]:
            total += int(data[curr_digit])
    return total


def main():
    with open('Day-01-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip()  # .split('\n')

    print(f'Day 01, Part 1--Solution to captcha is {solve_1(input_data)}')
    print(f'Day 01, Part 2--Solution to captcha is {solve_2(input_data)}')


if __name__ == '__main__':
    main()
