class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        squares = [0 for x in range(n)]
        highestSquareIdx= n-1
        left, right= 0, n-1
        while left <= right:
            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]
            if leftSquare > rightSquare:
                squares[highestSquareIdx] = leftSquare
                left += 1
            else:
                squares[highestSquareIdx] = rightSquare
                right -= 1
            highestSquareIdx -= 1
        return squares