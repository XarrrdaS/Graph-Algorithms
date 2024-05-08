def display_graph(graph, representation):
    if representation == 1 or representation == 3:
        for vertex, neighbors in enumerate(graph, start=1):
            print(f"Node {vertex}:")
            for neighbor_index, neighbor in enumerate(neighbors, start=1):
                if neighbor:
                    print(f"  - {neighbor_index}")
    elif representation == 2:
        for vertex, neighbors in enumerate(graph, start=1):
            print(f"Node {vertex}:")
            for neighbor in neighbors:
                print(f"  - {neighbor}")
    else:
        raise ValueError("Invalid graph representation!")