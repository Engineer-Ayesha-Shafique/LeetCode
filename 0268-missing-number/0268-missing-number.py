class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Calculate the expected sum of numbers from 0 to n using Gauss' formula
        expected_sum = n * (n + 1) // 2
        
        # Calculate the actual sum of elements in the array
        actual_sum = sum(nums)
        
        # The missing number is the difference between the expected sum and the actual sum
        return expected_sum - actual_sum
