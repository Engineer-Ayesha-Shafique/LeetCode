class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            previous_start, previous_end = merged[-1]

            # Check if the current interval overlaps with the previous one
            if current_start <= previous_end:
                # Merge the intervals by updating the end time
                merged[-1] = [previous_start, max(previous_end, current_end)]
            else:
                # Add a new interval to the result
                merged.append([current_start, current_end])

        return merged
