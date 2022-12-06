class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsLength = len(nums)
        result = []
        permutations = [[]]
        for currentNumber in nums:
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.pop(0)
                for j in range(len(oldPermutation)+1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, currentNumber)
                    if len(newPermutation) == numsLength:
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
        return result