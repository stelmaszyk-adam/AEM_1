import numpy as np
import math


nodes = []
distance_table = []


def distance(pt1, pt2):
    return math.sqrt((pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)


def convert_to_int_table(str_nodes):
    return [int(str_nodes[0]), int(str_nodes[1]), int(str_nodes[2])]


def tests_50_alg1_2():

    random_number_table = []

    for _ in range(50):

        random_number = np.random.randint(0, 100)
        while random_number in random_number_table:
            random_number = np.random.randint(0, 100)

        random_number_table.append(random_number)
        print("\n" + str(random_number))
        print("alg1: ")
        alg1(random_number)
        print("alg2: ")
        alg2(random_number)
        print("\n")


def alg1(init_node):
    localy_nodes = nodes[:]
    visited_nodes = []
    path_length = 0
    iterator = 50
    current_node = nodes[init_node]
    localy_nodes.remove(current_node)
    visited_nodes.append(current_node)

    while iterator > 0:
        min_length = -1
        min_neighbor = current_node

        for neighbor in localy_nodes:
            length = distance(current_node, neighbor)
            if min_length == -1 or min_length > length:
                min_length = length
                min_neighbor = neighbor

        path_length = path_length + min_length
        localy_nodes.remove(min_neighbor)
        visited_nodes.append(min_neighbor)
        current_node = min_neighbor

        iterator = iterator - 1

    length = distance(visited_nodes[0], visited_nodes[-1])
    path_length = path_length + length

    print(path_length)


def alg2(init_node):
    localy_nodes = nodes[:]
    visited_nodes = []
    path_length = 0
    iterator = 50
    current_node = nodes[init_node]
    localy_nodes.remove(current_node)
    visited_nodes.append(current_node)

    while iterator > 0:
        min_length = -1
        to_end_min_length = -1
        min_neighbor = current_node

        for neighbor in localy_nodes:
            length = distance(current_node, neighbor)
            to_end_length = distance(neighbor, nodes[init_node])
            if min_length == -1 or min_length + to_end_min_length > length + to_end_length:
                min_length = length
                to_end_min_length = to_end_length
                min_neighbor = neighbor

        path_length = path_length + min_length
        localy_nodes.remove(min_neighbor)
        visited_nodes.append(min_neighbor)
        current_node = min_neighbor

        iterator = iterator - 1
    
    length = distance(visited_nodes[0], visited_nodes[-1])
    path_length = path_length + length

    print(path_length)


def create_distance_table():
    for parent_node in nodes:
        helpful_table = []
        for child_node in nodes:
            helpful_table.append(distance(parent_node, child_node))

        distance_table.append(helpful_table)


with open("kroA100.txt", 'r') as instance:
    str_nodes = instance.readlines()
    nodes = [convert_to_int_table(line[:].replace(
        '\n', "").split(' ')) for line in str_nodes]


# create_distance_table()
# print(distance_table)
tests_50_alg1_2()
