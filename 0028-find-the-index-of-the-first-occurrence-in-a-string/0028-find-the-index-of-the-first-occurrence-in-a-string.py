class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If needle is an empty string, return 0
        if not needle:
            return 0

        # Iterate through the haystack string
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack starting from the current index matches needle
            if haystack[i:i+len(needle)] == needle:
                return i  # Return the index if a match is found

        return -1  # Return -1 if no match is found
