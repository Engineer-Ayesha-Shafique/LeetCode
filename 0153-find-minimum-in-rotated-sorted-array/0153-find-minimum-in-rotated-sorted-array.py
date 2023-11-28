class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1  # or any other appropriate value

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Check if the minimum element is in the left half or right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
