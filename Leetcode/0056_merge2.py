class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged = [intervals[0]]
        for i in range(len(intervals)):
            previous_end = merged[-1][1]
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            if previous_end >= current_start:      #overlap
                merged[-1][1] = max(previous_end, current_end)
            else:
                merged.append(intervals[i])
        return merged