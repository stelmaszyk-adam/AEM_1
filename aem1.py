import numpy as np
import math
import operator


nodes = []
distance_table = []


def distance(pt1, pt2):
    return math.sqrt((pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)


def convert_to_int_table(str_nodes):
    return [int(str_nodes[0]), int(str_nodes[1]), int(str_nodes[2])]


def tests_50_alg1_2_3():

    random_number_table = []

    table_result_1 = []
    table_result_2 = []
    table_result_3 = []

    for _ in range(50):

        random_number = np.random.randint(0, 100)
        while random_number in random_number_table:
            random_number = np.random.randint(0, 100)

        random_number_table.append(random_number)
        print("\n" + str(random_number))
        result_1 = alg1(random_number)
        table_result_1.append({"nodes": result_1, "length": calculate_path_dist(
            distance_table, result_1)})
        result_2 = alg2(random_number)
        table_result_2.append({"nodes": result_2, "length": calculate_path_dist(
            distance_table, result_2)})
        
        result_3 = alg3(random_number)
        table_result_3.append({"nodes": result_3, "length": calculate_path_dist(
            distance_table, result_3)})

    table_result_1 = sorted(table_result_1, key=lambda k: k['length'])
    # MIN
    print(table_result_1[0])
    # MAX
    print(table_result_1[-1])
    # AVG
    avg = (sum([result["length"] for result in table_result_1])) / \
        len(table_result_1)
    print(avg)

    table_result_2 = sorted(table_result_2, key=lambda k: k['length'])
    # MIN
    print(table_result_2[0])
    # MAX
    print(table_result_2[-1])
    # AVG
    avg = (sum([result["length"] for result in table_result_2])) / \
        len(table_result_2)
    print(avg)

    table_result_3 = sorted(table_result_3, key=lambda k: k['length'])
    # MIN
    print(table_result_3[0])
    # MAX
    print(table_result_3[-1])
    # AVG
    avg = (sum([result["length"] for result in table_result_3])) / \
        len(table_result_3)
    print(avg)


def find_closest_neighbor(node, localy_nodes):
    min_length = -1
    min_neighbor = node
    for neighbor in localy_nodes:
        length = distance_table[node][neighbor]
        if (min_length == -1 or min_length > length) and node != neighbor:
            min_length = length
            min_neighbor = neighbor

    return min_neighbor, min_length


def alg1(init_node):
    localy_nodes = [node[0]-1 for node in nodes]
    visited_nodes = []
    path_length = 0
    iterator = len(nodes)/2
    current_node = nodes[init_node][0]-1
    localy_nodes.remove(current_node)
    visited_nodes.append(current_node)

    while iterator > 1:

        min_neighbor, min_length = find_closest_neighbor(
            current_node, localy_nodes)

        path_length = path_length + min_length
        localy_nodes.remove(min_neighbor)
        visited_nodes.append(min_neighbor)
        current_node = min_neighbor

        iterator = iterator - 1

    length = distance_table[visited_nodes[0]][visited_nodes[-1]]
    path_length = path_length + length

    return visited_nodes


def alg2(init_node):
    localy_nodes = [node[0]-1 for node in nodes]
    visited_nodes = []
    iterator = len(nodes)/2
    current_node = nodes[init_node][0]-1
    localy_nodes.remove(current_node)
    visited_nodes.append(current_node)
    next_node, min_length = find_closest_neighbor(current_node, localy_nodes)
    localy_nodes.remove(next_node)
    visited_nodes.append(next_node)

    while iterator > 2:
        min_length = -1
        min_nodes_table = []
        min_node = next_node

        for neighbour in localy_nodes:
            for i in range(len(visited_nodes)):
                help_visited_nodes = visited_nodes[:]
                help_visited_nodes.insert(i, neighbour)
                length = calculate_path_dist(
                    distance_table, help_visited_nodes)

                if min_length == -1 or length < min_length:
                    min_length = length
                    min_node = neighbour
                    min_nodes_table = help_visited_nodes[:]

        localy_nodes.remove(min_node)

        visited_nodes = min_nodes_table[:]

        iterator = iterator - 1

    return visited_nodes


def alg3(init_node):
    localy_nodes = [node[0]-1 for node in nodes]
    visited_nodes = []
    iterator = len(nodes)/2
    current_node = nodes[init_node][0]-1
    localy_nodes.remove(current_node)
    visited_nodes.append(current_node)

    while iterator > 1:
        max_regret = -1
        min_length = -1
        min_nodes_table = []
        min_node = init_node

        for localy_node in localy_nodes:
            length = 0
            min_new_cycle = []
            min_length = -1
            min_second_length = -1

            for i in range(len(visited_nodes)):
                help_visited_nodes = visited_nodes[:]
                help_visited_nodes.insert(i, localy_node)
                length = calculate_path_dist(
                    distance_table, help_visited_nodes)

                if min_length == -1 or length < min_length:
                    min_length = length
                    min_new_cycle = help_visited_nodes[:]
                    continue

                if min_second_length == -1 or length < min_second_length:
                    min_second_length = length
            regret = np.abs(min_second_length - length)

            if max_regret == -1 or regret > max_regret:
                max_regret = regret
                min_nodes_table = min_new_cycle
                min_node = localy_node

        localy_nodes.remove(min_node)
        visited_nodes = min_nodes_table[:]
        iterator = iterator - 1

    return visited_nodes


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
tests_50_alg1_2_3()
# best_nodes, best_path_length = alg3(alg2(np.random.randint(0, 100)))

# print(best_nodes)
# print(best_path_length)
# alg3(np.random.randint(0, 100))
# alg1(np.random.randint(0, 100))
