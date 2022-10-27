class Solution(object):
    def binary_search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while (low<high):
            mid = int(low + math.floor((high-low+1)/2))
            if target < nums[mid]:
                high = mid-1
            else:
                low = mid
        return low if nums[low]==target else -1



        
