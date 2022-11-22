class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        full_arr = [item for item in range(1, max(arr)+1)]
        missingList = [x for x in full_arr if x not in arr]
        if k <= len(missingList):
            return missingList[k-1]
        else:
            return max(full_arr)+(k-len(missingList))