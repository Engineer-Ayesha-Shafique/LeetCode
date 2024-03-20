class Solution(object):
    def findRepeatedDnaSequences(self, dna_sequence):
        """
        :type s: str
        :rtype: List[str]
        """

        # Initialize a counter to keep track of the DNA sequence occurrences
        sequence_count = {}
        # Initialize an empty list to store the repeated sequences
        repeated_sequences = []
        # Calculate the number of possible substrings of length 10
        num_substrings = len(dna_sequence) - 10
        # Iterate over all the substrings of length 10 in the DNA sequence
        for i in range(num_substrings + 1):
            # Extract a substring of length 10
            subsequence = dna_sequence[i: i + 10]
            # If the count reaches 2, it means we've found a repeated sequence
            if sequence_count.get(subsequence) == 1:
                # Add it to the list of repeated sequences
                if subsequence not in repeated_sequences:
                    repeated_sequences.append(subsequence)
            # Increment the count for this particular substring
            else:
                sequence_count[subsequence] = 1
            
        # Return the list of repeated sequences
        return repeated_sequences
        
        