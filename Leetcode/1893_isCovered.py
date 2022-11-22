class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        rangeList = []
        for range_i in ranges:
            rangeList.append([item for item in range(range_i[0], range_i[1]+1)])  
        rangeList = set([item for sublist in rangeList for item in sublist])
        for i in range(left, right+1):
            if i not in rangeList:
                return False
        return True