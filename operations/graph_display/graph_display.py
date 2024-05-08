def display_graph(graph, representation):
    if representation == 1: 
        for row in graph:
            print(row)
    elif representation == 2:
        for node, neighbors in enumerate(graph):
            print(f"Node {node}: {neighbors}")
    elif representation == 3:
        for node, neighbors in enumerate(graph):
            print(f"Node {node}:")
            for neighbor in neighbors:
                print(f"  - {neighbor}")
    else:
        print("Invalid representation selected.")