class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if n >= nums[i] > 0 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1