from collections import deque

def bfs_matrix(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for i in range(len(graph[vertex])):
                if graph[vertex][i] == 1 and i not in visited:
                    queue.append(i)

def bfs_list(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

def bfs_table(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex)
            visited.append(vertex)
            for neighbor_index, neighbor in enumerate(graph[vertex - 1], start=1):
                if neighbor and neighbor_index not in visited:
                    queue.append(neighbor_index)

def bfs(graph, representation):

    choice = int(input('Where should program start looking form:\n> '))
    print('\n')

    if representation == 1:
        bfs_matrix(graph, choice)
    elif representation == 2:
        bfs_list(graph, choice)
    elif representation == 3:
        bfs_table(graph, choice)