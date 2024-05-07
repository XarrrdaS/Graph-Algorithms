def load_graph():
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = [[] for _ in range(num_vertices)]

    for vertex in range(num_vertices):
        successors = input(f"Podaj następników wierzchołka {vertex}: ").split()
        graph[vertex] = [int(successor) for successor in successors]

    return graph

def load_graph_heredoc():
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = [[] for _ in range(num_vertices)]

    input_data = input("Wprowadź dane za pomocą heredoc: ")
    lines = input_data.strip().split('\n')

    for vertex, line in enumerate(lines):
        successors = line.split()
        graph[vertex] = [int(successor) for successor in successors]

    return graph