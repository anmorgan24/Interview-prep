class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        maxStartHeap, maxEndHeap=[], []
        
        result = [0 for x in range(n)]
        for endIndex in range(n):
            heappush(maxStartHeap, (-intervals[endIndex][0], endIndex))
            heappush(maxEndHeap, (-intervals[endIndex][-1], endIndex))
            
        for _ in range(n):
            topEnd, endIndex = heappop(maxEndHeap)
            result[endIndex] = -1
            if -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
                while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                    topStart, startIndex = heappop(maxStartHeap)
                result[endIndex] = startIndex
                heappush(maxStartHeap, (topStart, startIndex))
                
        return result