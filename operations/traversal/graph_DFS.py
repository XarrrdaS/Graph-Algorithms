def dfs_matrix(graph, start):
    start = int(start) - 1
    visited = []
    stack = [start]

    while stack:
        vertex = int(stack.pop()) + 1
        if vertex not in visited:
            visited.append(vertex)
            neighbors = graph[vertex]
            stack.extend(neighbors)

    return visited

def dfs_list(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            neighbors = graph[vertex]
            stack.extend(neighbors)

    return visited

def dfs_table(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            neighbors = [neighbor_index for neighbor_index, neighbor in enumerate(graph[vertex - 1], start=1) if neighbor]
            stack.extend(neighbors)

    return visited

def dfs(graph, representation):
    while True:
        try:
            choice = int(input('Where should program start looking form:\n> '))
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
    print('\n')

    if representation == 1:
        print(dfs_matrix(graph, choice))
    elif representation == 2:
        print(dfs_list(graph, choice))
    elif representation == 3:
        print(dfs_table(graph, choice))