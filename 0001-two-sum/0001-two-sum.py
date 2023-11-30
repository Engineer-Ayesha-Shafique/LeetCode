class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of numbers
        num_dict = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_dict:
                # Return the indices of the two numbers
                return [num_dict[complement], i]

            # Add the current number and its index to the dictionary
            num_dict[num] = i

        # No solution found
        return None
