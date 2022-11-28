# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        allPaths = []
        self.find_paths_recursive(root, [], allPaths)
        
        return allPaths
    
    def find_paths_recursive(self, currentNode, currentPath, allPaths):
        if currentNode is None:
            return 
        
        currentPath.append(currentNode.val)
        
        if currentNode.left is None and currentNode.right is None:
            allPaths.append('->'.join(str(e) for e in currentPath))
            
        else:
            self.find_paths_recursive(currentNode.left, currentPath, allPaths)
            
            self.find_paths_recursive(currentNode.right, currentPath, allPaths)
            
        del currentPath[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print(str(binaryTreePaths(root)))


main()