class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
       
        def find_square_sum(n):
            _sum = 0
            while (n > 0):
                digit = n % 10
                _sum += digit * digit
                n //= 10
            return _sum
        
        slow, fast = n, n
        while True:
            slow = find_square_sum(slow)
            fast = find_square_sum(find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1