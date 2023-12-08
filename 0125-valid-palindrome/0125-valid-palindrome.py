import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase and remove non-alphanumeric characters
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        # Compare the original string with its reverse
        return cleaned_s == cleaned_s[::-1]

# Example usage:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))                      # Output: False
print(solution.isPalindrome(" "))                                # Output: True
