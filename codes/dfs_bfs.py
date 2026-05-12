from collections import deque

graph = {}

# input
n = int(input("Enter number of edges: "))

print("Enter edges:")
for _ in range(n):
    u, v = input().split()

    # create list if vertex not present
    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    # undirected graph
    graph[u].append(v)
    graph[v].append(u)


# DFS using recursion
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited)


# BFS using queue
def bfs(start):
    visited = set()
    q = deque([start])

    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)


start = input("Enter start node: ")

print("\nDFS Traversal:")
dfs(start, set())

print("\nBFS Traversal:")
bfs(start)  