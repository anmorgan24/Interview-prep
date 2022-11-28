# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        map = {}

        return self.count_paths_prefix_sum(root, targetSum, map, 0)
    
    def count_paths_prefix_sum(self, current_node, targetSum, map, current_path_sum):
       
        if current_node is None:
            return 0
        
        path_count = 0
        
        current_path_sum += current_node.val
        
        if targetSum == current_path_sum:
            path_count += 1
            
        path_count += map.get(current_path_sum - targetSum, 0)
        map[current_path_sum] = map.get(current_path_sum, 0) + 1
        
        path_count += self.count_paths_prefix_sum(current_node.left, targetSum, map, current_path_sum)
        path_count += self.count_paths_prefix_sum(current_node.right, targetSum, map, current_path_sum)
        
        map[current_path_sum] = map.get(current_path_sum, 1) - 1
        
        return path_count