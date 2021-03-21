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
        print("\n")
        print("alg2: ")

        best_nodes, best_path_length = alg3(alg2(random_number))

        print("\n")
        print("alg3: ")
        print(best_nodes)
        print(best_path_length)


def alg1(init_node):
    localy_nodes = nodes[:]
    visited_nodes = []
    path_length = 0
    iterator = len(nodes)/2
    current_node = nodes[init_node]
    localy_nodes.remove(current_node)
    visited_nodes.append(current_node)

    while iterator > 1:
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
    print([visited_node[0]-1 for visited_node in visited_nodes])


def alg2(init_node):
    localy_nodes = nodes[:]
    visited_nodes = []
    path_length = 0
    iterator = len(nodes)/2
    current_node = nodes[init_node]
    localy_nodes.remove(current_node)
    visited_nodes.append(current_node)

    while iterator > 1:
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
    print([visited_node[0]-1 for visited_node in visited_nodes])

    
    return [visited_node[0]-1 for visited_node in visited_nodes]


def alg3(init_nodes):
    best_nodes = init_nodes
    nodes_size = len(init_nodes)
    best_path_length = calculate_path_dist(distance_table, best_nodes)
    print(best_path_length)
    improvement_factor = 1

    while improvement_factor > 0.01:
        previous_best_length = best_path_length
        for swap_first in range(1, nodes_size - 2):
            for swap_last in range(swap_first + 1, nodes_size - 1):
                new_nodes = swap(best_nodes, swap_first, swap_last)
                new_path_length = calculate_path_dist(
                    distance_table, new_nodes)
                
                if 0 < best_path_length - new_path_length:
                    best_path_length = new_path_length
                    best_nodes = new_nodes

        improvement_factor = 1 - best_path_length/previous_best_length
    
    return best_nodes, best_path_length


def calculate_path_dist(distance_matrix, path):
    path_distance = 0
    for ind in range(len(path) - 1):
        path_distance += distance_matrix[path[ind]][path[ind + 1]]

    path_distance += distance_matrix[path[0]][path[-1]]
    return float("{0:.2f}".format(path_distance))


def swap(path, swap_first, swap_last):
    path_updated = np.concatenate((path[0:swap_first],
                                   path[swap_last:-
                                        len(path) + swap_first - 1:-1],
                                   path[swap_last + 1:len(path)]))
    return path_updated.tolist()


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


create_distance_table()
# print(distance_table)
tests_50_alg1_2()
# best_nodes, best_path_length = alg3(alg2(np.random.randint(0, 100)))

# print(best_nodes)
# print(best_path_length)
