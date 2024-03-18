class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        # Initialize Tribonacci sequence
        t0, t1, t2 = 0, 1, 1

        # Calculate Tribonacci numbers iteratively
        for _ in range(n - 2):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2