from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a dictionary to store groups of anagrams
        anagrams_dict = defaultdict(list)

        # Iterate through each word in the array
        for word in strs:
            # Sort the characters of the word and use it as a key in the dictionary
            sorted_word = ''.join(sorted(word))
            anagrams_dict[sorted_word].append(word)

        # Convert the values of the dictionary to a list to get the final result
        result = list(anagrams_dict.values())
        return result
