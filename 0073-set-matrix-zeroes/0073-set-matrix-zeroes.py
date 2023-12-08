class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        # Variables to check if the first row and first column need to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        first_col_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))

        # Use the first row and first column to store information about zeros
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set zeros based on information stored in the first row and first column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set zeros for the first row and first column if needed
        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
