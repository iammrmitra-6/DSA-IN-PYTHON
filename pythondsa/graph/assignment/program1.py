v,E=map(int,input().split())
matrix=[[0]*v for _ in range (v)]
adj=[[] for _ in range(v)]

for _ in range(E):
    u,v=map(int,input().split())
    matrix[u][v]=1
    matrix[v][u]=1
    adj[u].append(v)
    adj[v].append(u)

print("adjacency matrix :")
for row in matrix:
    print(*row)

print("adjacency matrix :")
for i in range(v):
    print(i,':',*sorted(adj[i]))

