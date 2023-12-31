class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        n = len(s)
        # Create a table to store whether a substring is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            is_palindrome[i][i] = True

        start, max_length = 0, 1

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                start = i
                max_length = 2

        # Check substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if is_palindrome[i + 1][j - 1] and s[i] == s[j]:
                    is_palindrome[i][j] = True
                    start = i
                    max_length = length

        return s[start:start + max_length]

