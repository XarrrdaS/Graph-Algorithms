def kahn_matrix(graph):
    n = len(graph)

    # Compute in-degree for each node
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            in_degree[j] += graph[i][j]

    # Initialize a queue with nodes that have 0 in-degree
    queue = [i for i in range(n) if in_degree[i] == 0]

    # Initialize the list for topological order
    top_order = []

    while queue:
        # Dequeue a node from queue and add it to topological order
        node = queue.pop(0)
        top_order.append(node + 1)  # Increase node by 1 before adding to top_order

        # Decrease in-degree by 1 for all its neighboring nodes
        for i in range(n):
            if graph[node][i] == 1:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

    # If topological sort is not possible
    if len(top_order) != n:
        print("Graph contains a cycle")
    # If topological sort is possible
    print("\n",top_order)

def kahn_list(graph):
    n = len(graph)

    # Compute in-degree for each node
    in_degree = [0] * n
    for node in graph:
        for neighbor in node:
            in_degree[neighbor] += 1

    # Initialize a queue with nodes that have 0 in-degree
    queue = [i for i in range(n) if in_degree[i] == 0]

    # Initialize the list for topological order
    top_order = []

    while queue:
        # Dequeue a node from queue and add it to topological order
        node = queue.pop(0)
        top_order.append(node + 1)  # Increase node by 1 before adding to top_order

        # Decrease in-degree by 1 for all its neighboring nodes
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # If in-degree becomes zero, add it to queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If topological sort is not possible
    if len(top_order) != n:
        print("Graph contains a cycle")
    # If topological sort is possible
    print("\n", top_order)
    return top_order


def kahn_table(graph):
    n = len(graph)

    # Compute in-degree for each node
    in_degree = [0] * n
    for node in range(n):
        for neighbor in graph[node]:
            in_degree[neighbor[0]] += 1

    # Initialize a queue with nodes that have 0 in-degree
    queue = [i for i in range(n) if in_degree[i] == 0]

    # Initialize the list for topological order
    top_order = []

    while queue:
        # Dequeue a node from queue and add it to topological order
        node = queue.pop(0)
        top_order.append(node + 1)  # Increase node by 1 before adding to top_order

        # Decrease in-degree by 1 for all its neighboring nodes
        for neighbor in graph[node]:
            in_degree[neighbor[0]] -= 1
            # If in-degree becomes zero, add it to queue
            if in_degree[neighbor[0]] == 0:
                queue.append(neighbor[0])

    # If topological sort is not possible
    if len(top_order) != n:
        print("Graph contains a cycle")
    # If topological sort is possible
    print("\n", top_order)
    return top_order

def kahn(graph, representation):
    if representation == 1:
        return kahn_matrix(graph)
    elif representation == 2:
        return kahn_list(graph)
    elif representation == 3:
        return kahn_table(graph)