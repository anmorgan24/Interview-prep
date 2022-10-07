class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while(left < right):
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right+ 1]
            
            if target > current_sum:
                left += 1
            else:
                right -= 1
        return [-1, -1]