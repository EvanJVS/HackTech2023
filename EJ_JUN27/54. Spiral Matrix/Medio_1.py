"""1) primer reto medio, dada una matriz que se entrega, devolver los valores en espiral
link: https://leetcode.com/problems/spiral-matrix/
"""
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16], [17,18,19,20]]

def spiral(matrix):
    lista = []
    if len(matrix) == 0:
        return lista 
    
    rows, cols = len(matrix), len(matrix[0])

    top, left = 0, 0
    bottom, right = rows - 1, cols - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            lista.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            lista.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                lista.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                lista.append(matrix[i][left])
            left += 1

    return lista

print(matrix)
print(spiral(matrix))

# Funciona, si, COMO, no se, lo vi de este video: https://www.youtube.com/watch?v=RLJCIQIAlQk







