import numpy as np
import re


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        array = np.array(board)
        for i in range(9):
            k = i//3*3
            j = (i % 3)*3
            row = "".join(np.sort(array[i, :])).replace(".", "")
            column = "".join(np.sort(array[:, i])).replace(".", "")
            grid = "".join(
                np.sort(array[k:k+3, j:j+3].flatten())).replace(".", "")

            if re.search("(\d)\\1+", row) or re.search("(\d)\\1+", column) or re.search("(\d)\\1+", grid):
                return False

        return True
