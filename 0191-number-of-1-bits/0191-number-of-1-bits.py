class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert the integer to a binary string and count the '1' bits
        
        binary_str = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
        return binary_str.count('1')

