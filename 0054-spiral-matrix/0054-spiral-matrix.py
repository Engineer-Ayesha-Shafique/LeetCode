class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        while matrix:
            # Append the first row from left to right
            result += matrix.pop(0)
            
            # Append the last column from top to bottom
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            
            # Append the last row from right to left
            if matrix:
                result += matrix.pop()[::-1]
            
            # Append the first column from bottom to top
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        
        return result
