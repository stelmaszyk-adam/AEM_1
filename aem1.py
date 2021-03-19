import numpy as np
import math


nodes = []


def distance(pt1, pt2):
    return math.sqrt((pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)


def convert_to_int_table(str_nodes):
    return [int(str_nodes[0]), int(str_nodes[1]), int(str_nodes[2])]


def alg1(init_node):
    # print(init_node)
    visited_nodes = []
    path_length = 0
    iterator = 50
    node = nodes[init_node]
    nodes.remove(node)

    

    while iterator > 0:
        
        # for nighbour
        
        # iterator = iterator - 1

    return


with open("kroA100.txt", 'r') as instance:
    str_nodes = instance.readlines()
    nodes = [convert_to_int_table(line[:].replace(
        '\n', "").split(' ')) for line in str_nodes]


alg1(np.random.randint(0, 100))

# print(str(distance([1, 1380, 939], [2, 2848, 96])))

# print(nodes)
