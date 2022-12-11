# Advent of Code 2017, Day-08
# https://adventofcode.com/2017


registers = {}


def fetch(reg: str) -> int:
    if reg not in registers.keys():
        registers[reg] = 0
    return registers[reg]


def should_do_command(condition_str: str) -> bool:
    reg, comparison, amt = condition_str.split(' ')
    a = fetch(reg)
    b = int(amt)
    switcher = {
        '==': a == b,
        '>': a > b,
        '<': a < b,
        '>=': a >= b,
        '<=': a <= b,
        '!=': a != b
    }
    return switcher.get(comparison, "Invalid Option")


def update_register(action_str: str):
    reg, op, amt = action_str.split(' ')
    if reg not in registers.keys():
        registers[reg] = 0
    if op == 'inc':
        registers[reg] += int(amt)
    else:
        registers[reg] -= int(amt)


def process(action_str: str, condition_str: str):
    # print(f'{action_str} <-- {condition_str}')
    if should_do_command(condition_str):
        update_register(action_str)


def run(program: list, part2=False) -> int:
    global registers
    registers = {}
    largest_ever = 0
    for input_line in program:
        action, condition = input_line.split(' if ')
        process(action, condition)
        if part2:
            largest = max(registers.values())
            if largest_ever < largest:
                largest_ever = largest
    if part2:
        return largest_ever
    else:
        return max(registers.values())


def main():
    with open('Day-08-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip().split('\n')

    print(f'Day 08, Part 1--Largest value in any register at the end is {run(input_data, False)}')
    print(f'Day 08, Part 2--Largest value in any register at any time is {run(input_data, True)}')


if __name__ == '__main__':
    main()
