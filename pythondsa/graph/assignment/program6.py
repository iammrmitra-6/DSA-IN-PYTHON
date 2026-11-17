import heapq

# Read vertices and edges
V, E = map(int, input().split())

# Build adjacency list for an undirected weighted graph: adj[u] = [(weight, v), ...]
adj = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    adj[v].append((w, u))

# Prim's Algorithm initialization starting from node 0
visited = [False] * V
visited[0] = True
heap = []

for w, v in adj[0]:
    heapq.heappush(heap, (w, 0, v))

mst = []
total = 0

# Process the priority queue
while heap and len(mst) < V - 1:
    w, u, v = heapq.heappop(heap)
    
    if visited[v]:
        continue
        
    visited[v] = True
    mst.append((u, v, w))
    total += w
    
    for nw, nv in adj[v]:
        if not visited[nv]:
            heapq.heappush(heap, (nw, v, nv))

# Check if MST exists (graph is connected)
if len(mst) != V - 1:
    print("MST does not exist: graph is disconnected.")
else:
    print("MST Edges (u-v : weight):")
    for u, v, w in mst:
        print(f"{u}-{v} : {w}")
    print("Total MST Weight:", total)