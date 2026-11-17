from collections import deque

# Read vertices and edges
V, E = map(int, input().split())

# Build adjacency list and indegree array for a directed graph
adj = [[] for _ in range(V)]
indegree = [0] * V

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    indegree[v] += 1  # Increment indegree for the destination vertex

# Initialize queue with all vertices having an indegree of 0
q = deque(i for i in range(V) if indegree[i] == 0)
order = []

# Process the queue
while q:
    u = q.popleft()
    order.append(u)
    
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

# Check if topological sort is possible (i.e., no cycles)
if len(order) == V:
    print("Topological Order:", *order)
else:
    print("Cycle detected: Topological ordering is not possible.")