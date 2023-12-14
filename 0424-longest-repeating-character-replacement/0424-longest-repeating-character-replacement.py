class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Initialize variables
        max_length = 0
        max_count = 0
        start = 0
        char_count = {}

        for end in range(len(s)):
            # Update the count of the current character
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            # Update the maximum count of any character in the current window
            max_count = max(max_count, char_count[s[end]])

            # If the length of the window minus the maximum count is greater than k,
            # shrink the window from the left
            if (end - start + 1 - max_count) > k:
                char_count[s[start]] -= 1
                start += 1

            # Update the maximum length of the repeating character substring
            max_length = max(max_length, end - start + 1)

        return max_length
