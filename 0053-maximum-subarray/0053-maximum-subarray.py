class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            # Choose between extending the current subarray or starting a new subarray
            current_sum = max(num, current_sum + num)
            # Update the maximum subarray sum
            max_sum = max(max_sum, current_sum)

        return max_sum