class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if lengths are different
        if len(s) != len(t):
            return False

        # Count occurrences of characters in string s
        char_count_s = {}
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        # Update counts based on characters in string t
        for char in t:
            if char not in char_count_s:
                return False
            char_count_s[char] -= 1
            if char_count_s[char] == 0:
                del char_count_s[char]

        # If all counts are zero, the strings are anagrams
        return not bool(char_count_s)

