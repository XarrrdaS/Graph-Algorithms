import numpy as np

def generate_dag(nodes, saturation):
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

def main():
    nodes = int(input("Podaj liczbę wierzchołków: "))
    saturation = float(input("Podaj wartość nasycenia (między 0 a 100): "))
    dag = generate_dag(nodes, saturation)
    print(dag)

if __name__ == "__main__":
    main()
