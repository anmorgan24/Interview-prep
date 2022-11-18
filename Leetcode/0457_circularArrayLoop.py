class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def find_next_index(nums, is_forward, current_index):
            direction = nums[current_index] >= 0
            
            if is_forward != direction:
                return -1 
            
            next_index = (current_index + nums[current_index]) % len(nums)
            
            if next_index == current_index:
                next_index = -1
                
            return next_index
        
        for i in range(len(nums)):
            is_forward = nums[i] >= 0
            slow, fast = i, i
            
            while True:
                slow = find_next_index(nums, is_forward, slow)
                fast = find_next_index(nums, is_forward, fast)
                if fast != -1:
                    fast = find_next_index(nums, is_forward, fast)
                if slow == -1 or fast == -1 or slow == fast:
                    break
                
            if slow != -1 and slow == fast:
                return True
        
        return False