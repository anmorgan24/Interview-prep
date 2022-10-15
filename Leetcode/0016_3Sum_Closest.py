class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        smallest_difference = 10001
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) -1
            
            while (left < right):
                target_diff = target-nums[i] - nums[left]-nums[right]
                
                if target_diff == 0: 
                    return target
                
                if abs(target_diff) < abs(smallest_difference) or (abs(target_diff)==abs(smallest_difference) and target_diff> smallest_difference):
                    smallest_difference = target_diff
                    
                if target_diff > 0:
                    left += 1
                    
                else:
                    right -= 1
                    
        return target - smallest_difference