class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0

        # Add intervals that come before the newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)  # Add the merged interval

        # Add intervals that come after the newInterval
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result

# Example usage:
intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]
solution = Solution()
output1 = solution.insert(intervals1, newInterval1)
print(output1)  # Output: [[1,5],[6,9]]

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]
output2 = solution.insert(intervals2, newInterval2)
print(output2)  # Output: [[1,2],[3,10],[12,16]]
