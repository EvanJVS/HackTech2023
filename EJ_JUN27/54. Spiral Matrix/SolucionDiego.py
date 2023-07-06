import numpy as np


class Solution(object):
    def spiralOrder(self, matrix):
        matrix = np.array(matrix)
        spiral = []
        while len(matrix.flatten()) != 0:
            spiral += list(matrix[0, :][::1])
            matrix = matrix[1:, :]
            if len(matrix.flatten()) == 0:
                break
            spiral += list(matrix[:, -1][::1])
            matrix = matrix[:, :-1]
            if len(matrix.flatten()) == 0:
                break
            spiral += list(matrix[-1, :][::-1])
            matrix = matrix[:-1, :]
            if len(matrix.flatten()) == 0:
                break
            spiral += list(matrix[:, 0][::-1])
            matrix = matrix[:, 1:]
        return spiral
