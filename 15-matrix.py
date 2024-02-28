import numpy as np

mat = [[5, 0], [1, -2]]

for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] *= 2

print(mat)

mat = np.array([[5, 0], [1, -2]])
print(mat * 2)
