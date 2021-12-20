import numpy as np

twoDArray = np.array([[1,2,3][4,5,6][7,8,9]])

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer-1
        for i in range(first,last):
            top = matrix[layer][i]
             