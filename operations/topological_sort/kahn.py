def kahn_matrix(graph):
    n = len(graph)

    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            in_degree[j] += graph[i][j]

    queue = [i for i in range(n) if in_degree[i] == 0]

    top_order = []

    while queue:
        node = queue.pop(0)
        top_order.append(node + 1)

        for i in range(n):
            if graph[node][i] == 1:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

    if len(top_order) != n:
        print("\nGraph contains a cycle")
    print("\n",top_order)

def kahn_list(graph):
    n = len(graph)

    in_degree = [0] * n
    for node in graph:
        for neighbor in node:
            in_degree[neighbor] += 1

    queue = [i for i in range(n) if in_degree[i] == 0]

    top_order = []

    while queue:
        node = queue.pop(0)
        top_order.append(node + 1)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) != n:
        print("\nGraph contains a cycle")
    print("\n", top_order)


def kahn_table(graph):
    n = len(graph)

    in_degree = [0] * n
    for node in range(n):
        for neighbor in graph[node]:
            in_degree[neighbor[0]] += 1

    queue = [i for i in range(n) if in_degree[i] == 0]

    top_order = []

    while queue:
        node = queue.pop(0)
        top_order.append(node + 1)

        for neighbor in graph[node]:
            in_degree[neighbor[0]] -= 1
            if in_degree[neighbor[0]] == 0:
                queue.append(neighbor[0])

    if len(top_order) != n:
        print("\nGraph contains a cycle")
    print("\n", top_order)

def kahn(graph, representation):
    if representation == 1:
        kahn_matrix(graph)
    elif representation == 2:
        kahn_list(graph)
    elif representation == 3:
        kahn_table(graph)