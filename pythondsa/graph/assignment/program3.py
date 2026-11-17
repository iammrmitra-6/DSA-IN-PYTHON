def dfs(u, adj, visited, order):
    visited[u] = True
    order.append(u)
    for v in sorted(adj[u]):
        if not visited[v]:
            dfs(v, adj, visited, order)

# Read vertices and edges
V, E = map(int, input().split())

# Build adjacency list for an undirected graph
adj = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Perform DFS from a given source node
source = int(input())
visited = [False] * V
order = []
dfs(source, adj, visited, order)
print("DFS Traversal:", *order)

# Count and find connected components
visited = [False] * V
components = 0
for vertex in range(V):
    if not visited[vertex]:
        components += 1
        temp = []
        dfs(vertex, adj, visited, temp)

print("Connected Components:", components)