import numpy as np
import math


def det_node(a,b,c):
    return a[1]*b[2]+b[1]*c[2]+c[1]*a[2]-c[1]*b[2]-b[1]*a[2]-a[1]*c[2]

def crossing(path1, path2):
    node1, node2 = path1
    node3, node4 = path2
    n = det_node(node1,node2,node3) * det_node(node1,node2,node4)
    if n > 0:
        return False
    else:
        return True


nodes = []

def distance(pt1, pt2):
    return math.sqrt((pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)

def convert_to_int_table(str_nodes):
    return [int(str_nodes[0]), int(str_nodes[1]), int(str_nodes[2])]

def tests_50_alg1():

    random_number_table = []
    sum = 0
    for _ in range(50):

        random_number = np.random.randint(0, 100)
        while random_number in random_number_table:
            random_number = np.random.randint(0, 100)

        random_number_table.append(random_number)
        #print("\n" + str(random_number))
        
        sum+=alg2(random_number)
    print(sum/50)

def path_length(nodess):
    l = 0
    for i in range(len(nodess)-1):
        l+=distance(nodess[i],nodess[i+1])
    l+=distance(nodess[len(nodess)-1],nodess[0])
    return l

max_value = 6**9
Dist_Matrix = [[distance(i,j) for j in nodes] for i in nodes]
for i in range(len(nodes)):
    Dist_Matrix[i,i] = max_value

def swap_nodes(nodes,i,j):
    

def check(nodes):
    n = len(nodes)
    still_crossing=True
    while still_crossing:
        crossing_detected=False
        while not crossing_detected:
            for i in range(n-3):
                for j in range(i+2, n-1):
                    still_crossing=False
                    path1 = [nodes[i], nodes[i+1]]
                    path2 = [nodes[j], nodes[j+1]]

                    if crossing(path1, path2):
                        crossing_detected=True
                        still_crossing=True
                        nodes = swap_nodes(nodes,i,j)
    return nodes


def alg2(init_node):
    localy_nodes = nodes[:]
    visited_nodes = []
    iterator = 50
    localy_nodes.remove(nodes[init_node])
    visited_nodes.append(nodes[init_node])
    current_node = nodes[init_node]

    while iterator > 0:
        min_length = -1
        min_neighbor = current_node

        for neighbor in localy_nodes:
            length = distance(current_node, neighbor)
            if min_length == -1 or min_length > length:
                min_length = length
                min_neighbor = neighbor

        localy_nodes.remove(min_neighbor)
        visited_nodes.append(min_neighbor)
        current_node = visited_nodes[len(visited_nodes)-1]

        check(visited_nodes)


        iterator -= 1

    return path_length(visited_nodes)


        





with open("kroA100.txt", 'r') as instance:
    str_nodes = instance.readlines()
    nodes = [convert_to_int_table(line[:].replace(
        '\n', "").split(' ')) for line in str_nodes]


tests_50_alg1()

