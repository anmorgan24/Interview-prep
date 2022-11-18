class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        timeList = [[timeSeries[0], timeSeries[0] + duration]]
        for i in range(1, len(timeSeries)):
            previous_end = timeList[-1][1]
            current_start = timeSeries[i]
            current_end = timeSeries[i] + duration
            if previous_end >= current_start:      #overlap
                timeList[-1][1] = max(previous_end, current_end)
            else:
                timeList.append([timeSeries[i], timeSeries[i] + duration])
        totalTime = 0
        for tup in timeList:
            totalTime += (tup[1]- tup[0])
        return totalTime