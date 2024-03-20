class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity: O(n2). 
        # Use of a nested loop (one for iterating, other for two-pointer technique) brings the time complexity to O(n2).
        # Auxiliary Space: O(1). 
        # As no use of additional data structure is used.

        # Sort the array to easily skip duplicates
        nums.sort()

        # Initialize an empty list to store the result triplets
        result = []

        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1

            # Check for triplets
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers
                    left += 1
                    right -= 1

        return result
