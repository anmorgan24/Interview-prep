class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nextElement = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nextElement] = nums[i]
                nextElement += 1
        return nextElement