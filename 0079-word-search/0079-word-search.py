class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(row, col, index):
            # Base case: If the entire word is found
            if index == len(word):
                return True
            
            # Check if the current position is within the board and the letter matches
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == word[index]:
                # Mark the current cell as visited
                temp, board[row][col] = board[row][col], '/'
                
                # Explore adjacent cells in all four directions
                if (backtrack(row + 1, col, index + 1) or
                    backtrack(row - 1, col, index + 1) or
                    backtrack(row, col + 1, index + 1) or
                    backtrack(row, col - 1, index + 1)):
                    return True
                
                # Backtrack: restore the original value and unmark the cell
                board[row][col] = temp
                
            return False

        # Iterate through each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        # If no match is found
        return False
