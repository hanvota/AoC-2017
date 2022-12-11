# Advent of Code 2017, Day-05
# https://adventofcode.com/2017


def maze_1(program: list) -> int:
    steps = 0
    pc = 0
    program_length = len(program)

    while pc < program_length:
        # print(f'{program[pc]}')
        move = program[pc]
        program[pc] += 1
        pc += move
        steps += 1

    return steps


def maze_2(program: list) -> int:
    steps = 0
    pc = 0
    program_length = len(program)

    while pc < program_length:
        # print(f'{program[pc]}')
        move = program[pc]
        if move >= 3:
            program[pc] -= 1
        else:
            program[pc] += 1
        pc += move
        steps += 1

    return steps


def main():
    with open('Day-05-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip().split('\n')
    input_data = list(map(int, input_data))
    print(f'Day 05, Part 1--Exit is reached in {maze_1(input_data)} steps')

    with open('Day-05-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip().split('\n')
    input_data = list(map(int, input_data))

    print(f'Day 05, Part 2--Exit is reached in {maze_2(input_data)} steps')


if __name__ == '__main__':
    main()
