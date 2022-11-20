class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i, j, = 0, 0
        
        while i < len(firstList) and j < len(secondList):
            a_overlaps_b = firstList[i][0] >= secondList[j][0] and \
            firstList[i][0] <= secondList[j][1]
            
            b_overlaps_a = secondList[j][0] >= firstList[i][0] and \
            secondList[j][0] <= firstList[i][1]
            
            if a_overlaps_b or b_overlaps_a:
                result.append([max(firstList[i][0], secondList[j][0]), \
                               min(firstList[i][1], secondList[j][1])])
                
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return result