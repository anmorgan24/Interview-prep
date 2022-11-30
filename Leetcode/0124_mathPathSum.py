# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.globalMaximumSum = -float('inf')
        self.maxPathSumRecursive(root)
        return self.globalMaximumSum
    
    def maxPathSumRecursive(self, currentNode):
        if currentNode is None:
            return 0
        maxPathSumFromLeft = self.maxPathSumRecursive(currentNode.left)
        maxPathSumFromRight = self.maxPathSumRecursive(currentNode.right)
        
        maxPathSumFromLeft = max(maxPathSumFromLeft, 0)
        maxPathSumFromRight = max(maxPathSumFromRight, 0)
        
        localMaximumSum = maxPathSumFromLeft + maxPathSumFromRight + currentNode.val
        
        self.globalMaximumSum = max(self.globalMaximumSum, localMaximumSum)
        
        return max(maxPathSumFromLeft, maxPathSumFromRight) + currentNode.val