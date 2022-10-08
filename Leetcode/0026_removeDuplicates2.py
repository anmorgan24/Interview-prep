class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        next_non_duplicate=1
    
        while (i< len(nums)):
            if nums[next_non_duplicate-1] != nums[i]:
                nums[next_non_duplicate] = nums[i]
                next_non_duplicate += 1
            i += 1
        return next_non_duplicate