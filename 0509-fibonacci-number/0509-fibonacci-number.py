class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        mem=[0,1]

        for i in range(1,n):
            mem=[mem[1], mem[1]+mem[0]]

        return mem[-1]
        
        