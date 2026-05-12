from collections import defaultdict, deque

# graph using adjacency list
graph = defaultdict(list)

# input
n = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(n):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)   # undirected graph

# DFS (recursive)
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited)

# BFS (iterative)
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