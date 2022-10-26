class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [False] * (n+1)
        for i in range(1, n+1):
            for j in range(i, n+1, i):
                bulbs[j] = not bulbs[j]
        return sum(bulbs)