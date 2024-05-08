def tarjan_matrix(graph):
    stack = []
    low = [0] * len(graph)
    visited = [False] * len(graph)
    result = []

    def strongconnect(node):
        low[node-1] = len(stack)
        stack.append(node)
        visited[node-1] = True

        for successor in range(1, len(graph)+1):
            if graph[node-1][successor-1] == 1:
                if not visited[successor-1]:
                    strongconnect(successor)
                    low[node-1] = min(low[node-1], low[successor-1])
                elif successor in stack:
                    low[node-1] = min(low[node-1], low[successor-1])

        if low[node-1] == stack.index(node):
            connected_component = []

            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node:
                    break

            result.append(connected_component)

    for node in range(1, len(graph)+1):
        if not visited[node-1]:
            strongconnect(node)

    print("\n",result)

def tarjan_list(graph):
    stack = []
    low = [0] * (len(graph) + 1)
    visited = [False] * (len(graph) + 1)
    result = []

    def strongconnect(node):
        low[node] = len(stack)
        stack.append(node)
        visited[node] = True

        for successor in graph[node-1]:
            if not visited[successor]:
                strongconnect(successor)
                low[node] = min(low[node], low[successor])
            elif successor in stack:
                low[node] = min(low[node], low[successor])

        if low[node] == stack.index(node):
            connected_component = []

            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node:
                    break

            result.append(connected_component)

    for node in range(1, len(graph)+1):
        if not visited[node]:
            strongconnect(node)

    print("\n",result)

def tarjan_table(graph):
    flattened_graph = [edge for sublist in graph for edge in sublist]

    valid_edges = [edge for edge in flattened_graph if len(edge) >= 2 and isinstance(edge[0], int) and isinstance(edge[1], int)]

    for edge in flattened_graph:
        if len(edge) < 2 or not isinstance(edge[0], int) or not isinstance(edge[1], int):
            print(f"Invalid edge: {edge}")

    if not valid_edges:
        return []

    nodes = max(max(edge[0], edge[1]) for edge in valid_edges) + 1

    stack = []
    low = [0] * nodes
    visited = [False] * nodes
    result = []

    def strongconnect(node):
        low[node] = len(stack)
        stack.append(node)
        visited[node] = True

        for edge in valid_edges:
            if edge[0] == node:
                successor = edge[1]
                if not visited[successor]:
                    strongconnect(successor)
                    low[node] = min(low[node], low[successor])
                elif successor in stack:
                    low[node] = min(low[node], low[stack.index(successor)])

        if low[node] == stack.index(node):
            connected_component = []

            while True:
                successor = stack.pop()
                connected_component.append(successor + 1)
                if successor == node:
                    break

            result.append(connected_component)

    for node in range(nodes):
        if not visited[node]:
            strongconnect(node)

    print("\n",result)

def tarjan(graph, representation):
    if representation == 1:
        tarjan_matrix(graph)
    elif representation == 2:
        tarjan_list(graph)
    elif representation == 3:
        tarjan_table(graph)