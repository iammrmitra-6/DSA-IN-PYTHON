def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

# Read vertices and edges
V, E = map(int, input().split())

# Read edges and store as (weight, u, v)
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges by weight
edges.sort()

# DSU structures
parent = list(range(V))
rank = [0] * V
mst = []
total = 0

# Kruskal's algorithm loop
for w, u, v in edges:
    if union(parent, rank, u, v):
        mst.append((u, v, w))
        total += w
        if len(mst) == V - 1:
            break

# Check if MST exists (graph is connected)
if len(mst) != V - 1:
    print("MST does not exist: graph is disconnected.")
else:
    print("MST Edges (u-v : weight):")
    for u, v, w in mst:
        print(f"{u}-{v} : {w}")
    print("Total MST Weight:", total)