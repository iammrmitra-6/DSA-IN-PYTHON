A=[[1, 2], [4, 5]]
B=[[7, 8], [9, 10]]
rows = len(A)
cols = len(A[0])
C =[[0 for i in range(cols)] for j in range(rows)]
# Matrix Addition using nested loops
for i in range(rows):
    for j in range(cols):
        C[i][j] = A[i][j] + B[i][j]
print("Addition using nested lists:\\n", C)
# Output:
# Addition using nested lists:
# [[8, 10], [13, 15]]
