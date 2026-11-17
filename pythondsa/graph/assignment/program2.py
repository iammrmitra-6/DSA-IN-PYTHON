from collections import deque

# Read number of vertices (V) and edges (E)
V, E = map(int, input().split())

# Build the adjacency list for an undirected graph
adj = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Read the starting vertex
start = int(input())

# Initialize BFS structures
visited = [False] * V
q = deque([start])
visited[start] = True
order = []

# Perform BFS traversal
while q:
    u = q.popleft()
    order.append(u)
    
    # Explore neighbors in sorted order
    for v in sorted(adj[u]):
        if not visited[v]:
            visited[v] = True
            q.append(v)

# Print the final traversal order
print("Traversal order:", order)