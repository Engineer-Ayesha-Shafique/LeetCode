class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Initialize an array to store the count of set bits for each number
        bits_count = [0] * (n + 1)

        for i in range(1, n + 1):
            # The count of set bits for a number 'i' is equal to the count of set bits for i/2
            # If i is even, the count remains the same as i/2
            # If i is odd, add 1 to the count of set bits for i/2
            bits_count[i] = bits_count[i // 2] + (i % 2)

        return bits_count
