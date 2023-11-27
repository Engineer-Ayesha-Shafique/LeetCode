class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize variables to keep track of the maximum and minimum product ending at each index
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for num in nums[1:]:
            # If the current number is negative, swap max_product and min_product
            if num < 0:
                max_product, min_product = min_product, max_product

            # Update max_product and min_product for the current index
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            # Update the overall result
            result = max(result, max_product)

        return result