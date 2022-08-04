class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # abstracted
        if not root:
            return None
        
        # switch
        
        temp = root.left
        
        root.left = root.right
        
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root