class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i, j, start, end = 0, 0, 0, 1
        
        while i < len(firstList) and j < len(secondList):
            a_overlaps_b = firstList[i][start] >= secondList[j][start] and \
            firstList[i][start] <= secondList[j][end]
            
            b_overlaps_a = secondList[j][start] >= firstList[i][start] and \
            secondList[j][start] <= firstList[i][end]
            
            if a_overlaps_b or b_overlaps_a:
                result.append([max(firstList[i][start], secondList[j][start]), \
                               min(firstList[i][end], secondList[j][end])])
                
            if firstList[i][end] < secondList[j][end]:
                i += 1
            else:
                j += 1
                
        return result