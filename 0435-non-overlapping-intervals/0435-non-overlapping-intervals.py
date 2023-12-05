class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # Sort intervals based on end points
        intervals.sort(key=lambda x: x[1])

        # Initialize variables
        non_overlapping_count = 1
        end = intervals[0][1]

        # Iterate through intervals and find non-overlapping intervals
        for interval in intervals[1:]:
            if interval[0] >= end:
                non_overlapping_count += 1
                end = interval[1]

        # Calculate the number of intervals to remove
        to_remove = len(intervals) - non_overlapping_count
        return to_remove

