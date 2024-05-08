import numpy as np

def generate_dag_matrix(nodes, saturation):
    adjacency_matrix = np.zeros((nodes, nodes))

    saturation = saturation / 100

    edges = int(saturation * nodes * (nodes - 1))
    i = 0
    while edges > 0 and i < nodes:
        for j in range(i+1, nodes):
            if edges > 0:
                adjacency_matrix[i, j] = 1
                edges -= 1
        i += 1

    return adjacency_matrix

def generate_dag_list(nodes, saturation):
    adjacency_list = [[] for _ in range(nodes)]

    saturation = saturation / 100

    edges = int(saturation * nodes * (nodes - 1))
    i = 0
    while edges > 0 and i < nodes:
        for j in range(i+1, nodes):
            if edges > 0:
                adjacency_list[i].append(j)
                edges -= 1
        i += 1

    return adjacency_list

def generate_dag_table(nodes, saturation):
    adjacency_table = [[] for _ in range(nodes)]

    saturation = saturation / 100

    edges = int(saturation * nodes * (nodes - 1))
    i = 0
    while edges > 0 and i < nodes:
        for j in range(i+1, nodes):
            if edges > 0:
                adjacency_table[i].append((j, 1))
                edges -= 1
        i += 1

    return adjacency_table

def generate(representation):
    nodes = int(input("Podaj liczbę wierzchołków:\n> "))
    saturation = float(input("Podaj wartość nasycenia (między 0 a 100):\n> "))
    
    if representation == 1:
        adjacency_matrix = generate_dag_matrix(nodes, saturation)
        return adjacency_matrix
    elif representation == 2:
        adjacency_list = generate_dag_list(nodes, saturation)
        return adjacency_list
    elif representation == 3:
        adjacency_table = generate_dag_table(nodes, saturation)
        return adjacency_table