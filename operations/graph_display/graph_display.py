def display_graph(graph, representation):

    if representation == 1: 
        print("   ", end="")
        for i in range(len(graph[0])):
            print(f" {i+1} ", end="")
        print()
        print("-" * (4 * len(graph[0])))
        for i, row in enumerate(graph):
            if i < 9:
                print(f"{i+1} | ", end="")
            else:
                print(f"{i+1}| ", end="")
            for element in row:
                print(f" {int(element)} ", end="")
            print()
            
    elif representation == 2:
        for node, neighbors in enumerate(graph):
            print(f"Node {node+1}: {neighbors}")

    elif representation == 3:
        for vertex, neighbors in enumerate(graph, start=1):
            print(f"Node {vertex}:")
            for neighbor_index, neighbor in enumerate(neighbors, start=1):
                if neighbor:
                    print(f"  - {neighbor_index}")


    else:
        print("Invalid representation selected.")