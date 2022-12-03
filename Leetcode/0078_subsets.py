class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for currentNumber in nums:
            for i in range(len(subsets)):
                set1 = list(subsets[i])
                set1.append(currentNumber)
                subsets.append(set1)
        return subsets