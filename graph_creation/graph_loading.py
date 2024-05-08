def load_graph(representation):
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = None

    if representation == 2:
        graph = [[] for _ in range(num_vertices)]
    elif representation == 1:
        graph = [[0] * num_vertices for _ in range(num_vertices)]
    elif representation == 3:
        graph = [[False] * num_vertices for _ in range(num_vertices)]
    else:
        raise ValueError("Nieprawidłowa reprezentacja grafu")

    for vertex in range(num_vertices):
        successors = input(f"Podaj następniki wierzchołka {vertex+1}: ").split()

        if representation == 2:
            graph[vertex] = [int(successor) for successor in successors]
        elif representation == 1:
            for successor in successors:
                graph[vertex][int(successor) - 1] = 1
        elif representation == 3:
            for successor in successors:
                graph[vertex][int(successor) - 1] = True

    return graph

def load_graph_heredoc(representation):
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = None

    if representation == 2:
        graph = [[] for _ in range(num_vertices)]
    elif representation == 1:
        graph = [[0] * num_vertices for _ in range(num_vertices)]
    elif representation == 3:
        graph = [[False] * num_vertices for _ in range(num_vertices)]
    else:
        raise ValueError("Nieprawidłowa reprezentacja grafu")

    input_data = input("Wprowadź dane za pomocą heredoc: ")
    lines = input_data.strip().split('\n')

    for vertex, line in enumerate(lines):
        successors = line.split()

        if representation == 2:
            graph[vertex] = [int(successor) for successor in successors]
        elif representation == 1:
            for successor in successors:
                graph[vertex][int(successor)] = 1
        elif representation == 3:
            for successor in successors:
                graph[vertex][int(successor)] = True

    return graph