# Advent of Code 2017, Day-12
# https://adventofcode.com/2017

from dataclasses import dataclass


@dataclass
class Node:
    id: int
    parent = None
    children = []


def find_node(node_id, nodes):
    for node in nodes:
        if node['id'] == node_id:
            return node
    return None


def make_new_node(node_id):
    new_node = dict()
    new_node['id'] = node_id
    new_node['parent'] = None
    new_node['children'] = []
    return new_node


def backtracking(nodes, root):
    count = 0  # number of nodes that can reach root.

    for node in nodes:
        path = [node['id']]

        if node['id'] == root:
            path.append('At -0-')
            print(path)
            count += 1
            continue
        visited = {node['id']}
        n = node
        while True:
            p_id = n['parent']

            if p_id == root:
                count += 1
                path.append('0')
                print(path)
                break
            if p_id in visited:  # we have been here before, so we are in an endless loop
                path.append('Been here. Done')
                print(path)
                break
            n = find_node(p_id, nodes)
            if n is None:  # a branch that ends without reaching root '0'
                path.append('at root but NOT -0-')
                print(path)
                break
            path.append(p_id)
            visited.add(p_id)

    return count


def solve_1(data):
    nodes = list()
    for input_line in data:
        # print(f'{input_line}')
        p_id, r_side = input_line.split(' <-> ')
        children = r_side.split(',')
        # print(p_id, '---', children)
        node = find_node(p_id, nodes)
        if node is None:
            node = make_new_node(p_id)
            nodes.append(node)
        # fill in node parameters
        for c_id in children:
            c_id = c_id.lstrip()
            child = find_node(c_id, nodes)
            if child is None:
                child = make_new_node(c_id)
                nodes.append(child)
            if child['parent'] is None:
                child['parent'] = p_id
            node['children'].append(c_id)
        # print('new node- ', node)
    nodes[0]['parent'] = None
    print()
    for n in nodes:
        print('node: ', n['id'])
        p = n['parent']
        print('  parent-', n['parent'])
        for c in n['children']:
            print('----child: ', c)

    num_program = backtracking(nodes, '0')
    return num_program


def main():
    with open('Day-12-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_data = f.read().strip().split('\n')

    print(f'Day 12, Part 1--Number of programs connected to ID 0 is {solve_1(input_data)}')
    # print(f'Day 12, Part 2--')


if __name__ == '__main__':
    main()
