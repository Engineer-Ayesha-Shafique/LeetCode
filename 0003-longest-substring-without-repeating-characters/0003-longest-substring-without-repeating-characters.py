class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to store the last index of each character
        char_index = {}
        
        # Initialize variables for the sliding window
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            # If the character is already in the dictionary and its last index is after the start of the current window
            if s[end] in char_index and char_index[s[end]] >= start:
                # Move the start of the window to the next index after the last occurrence of the current character
                start = char_index[s[end]] + 1
            
            # Update the last index of the current character
            char_index[s[end]] = end
            
            # Update the maximum length if needed
            max_length = max(max_length, end - start + 1)
        
        return max_length
