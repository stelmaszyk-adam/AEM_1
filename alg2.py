import numpy as np
import math


#det_node = lambda a,b,c: a[1]*b[2]+b[1]*c[2]+c[1]*a[2]-c[1]*b[2]-b[1]*a[2]-a[1]*c[2]
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



def alg2(init_node):
    localy_nodes = nodes[:]
    visited_nodes = []
    iterator = 50
    localy_nodes.remove(nodes[init_node])
    visited_nodes.append(nodes[init_node])


    while iterator > 0:
        min_length = -1
        for neighbor in localy_nodes:
            for node in visited_nodes:
                length = distance(node, neighbor)
                if min_length == -1 or min_length > length:
                    min_length = length
                    min_neighbor = neighbor
                    first_node = node
        
        # sprawdzam które node są połączone z tym najbliższym
        fn = visited_nodes.index(first_node)
        if fn==len(visited_nodes)-1:
            n1 = visited_nodes[fn-1]
            n2 = visited_nodes[0]
        elif fn==0:
            n1 = visited_nodes[len(visited_nodes)-1]
            n2 = visited_nodes[1]
        else:
            n1 = visited_nodes[fn-1]
            n2 = visited_nodes[fn+1]

        if distance(n1, min_neighbor)>distance(n2, min_neighbor):
            second_node = n2
        else:
            second_node = n1
        

        localy_nodes.remove(min_neighbor)
        f1 = visited_nodes.index(first_node)
        f2 = visited_nodes.index(second_node)

        if f1<f2:
            if f2 == len(visited_nodes)-1:
                visited_nodes.append(min_neighbor)
            else:
                visited_nodes.insert(f2, min_neighbor)
        else:
            if f1 == len(visited_nodes)-1:
                visited_nodes.append(min_neighbor)
            else:
                visited_nodes.insert(f1, min_neighbor)
        iterator = iterator - 1

    return path_length(visited_nodes)


        





with open("kroA100.txt", 'r') as instance:
    str_nodes = instance.readlines()
    nodes = [convert_to_int_table(line[:].replace(
        '\n', "").split(' ')) for line in str_nodes]


tests_50_alg1()

