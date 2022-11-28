# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        allPaths = []
        self.find_paths_recursive(root, [], allPaths)
        return sum(allPaths)


    def find_paths_recursive(self, currentNode, currentPath, allPaths):
        if currentNode is None:
            return

        # add the current node to the path
        currentPath.append(currentNode.val)

        # if the current node is a leaf and its value is equal to required_sum,         save the current path
        if currentNode.left is None and currentNode.right is None:
            allPaths.append(int(''.join(str(e) for e in list(currentPath))))
        else:
            # traverse the left sub-tree
            self.find_paths_recursive(currentNode.left, currentPath, allPaths)
            # traverse the right sub-tree
            self.find_paths_recursive(currentNode.right, currentPath, allPaths)

        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        del currentPath[-1]