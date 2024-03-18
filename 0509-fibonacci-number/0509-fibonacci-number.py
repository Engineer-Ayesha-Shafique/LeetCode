class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        if n < 2:
            return int(n)
        else:
            for i in range(2, n+1):
                c = a + b
                a = b
                b = c
            return b
        
        