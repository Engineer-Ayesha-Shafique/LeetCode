class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check for an empty list
        if not nums:
            return 0

        # Initialize pointers
        slow_ptr = 0

        # Iterate through the array with fast pointer
        for fast_ptr in range(1, len(nums)):
            # If the current element is different from the previous one, update slow_ptr
            if nums[fast_ptr] != nums[slow_ptr]:
                slow_ptr += 1
                nums[slow_ptr] = nums[fast_ptr]

        # The length of the unique elements is (slow_ptr + 1)
        return slow_ptr + 1
