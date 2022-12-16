class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        parenthesesString = [0 for x in range(2*n)]
        self.generate_valid_parentheses_rec(n, 0, 0, parenthesesString, 0, result)
        return result

    def generate_valid_parentheses_rec(self, n, openCount, closeCount, parenthesesString, index, result):

        if openCount == n and closeCount == n:
            result.append(''.join(parenthesesString))
        else:
            if openCount < n:
                parenthesesString[index] = '('
                self.generate_valid_parentheses_rec(n, openCount + 1, closeCount, parenthesesString, index + 1, result)

            if openCount > closeCount:
                parenthesesString[index] = ')'
                self.generate_valid_parentheses_rec(n, openCount, closeCount + 1, parenthesesString, index + 1, result)