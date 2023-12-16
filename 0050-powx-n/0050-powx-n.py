class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            x = 1 / x
            n = -n
        
        # Use recursive approach with the divide-and-conquer strategy
        half_pow = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return half_pow * half_pow
        else:
            return half_pow * half_pow * x

