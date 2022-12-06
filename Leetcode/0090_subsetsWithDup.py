class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list.sort(nums)
        subsets = [[]]
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                startIndex = endIndex + 1
            else:
                startIndex = 0

            endIndex = len(subsets) - 1
            for j in range(startIndex, endIndex + 1):
                set1 = list(subsets[j])
                set1.append(nums[i])
                subsets.append(set1)
        return subsets