class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = []
        permutations.append(s)
        for i in range(len(s)):
            if s[i].isalpha():
                n = len(permutations)
                for j in range(n):
                    chs = list(permutations[j])
                    chs[i] = chs[i].swapcase()
                    permutations.append(''.join(chs))
        return permutations