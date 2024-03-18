class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array to store the number of ways to reach each step
        ways = [0] * n
        ways[0] = 1
        ways[1] = 2
        print(ways)

        # Calculate the number of ways for each step from 3 to n
        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]
            print(ways)

        return ways[n - 1]
    
    
