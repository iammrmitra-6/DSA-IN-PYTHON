def topo_dfs(u, adj, visited, stack):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            topo_dfs(v, adj, visited, stack)
    stack.append(u)

# Read vertices and edges
V, E = map(int, input().split())

# Build adjacency list for a directed graph
adj = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)  # Directed edge from u to v

# Perform Topological Sort using DFS
visited = [False] * V
stack = []

for u in range(V):
    if not visited[u]:
        topo_dfs(u, adj, visited, stack)

# Print the topological order (reverse of the finish order)
print("Topological Order:", *reversed(stack))