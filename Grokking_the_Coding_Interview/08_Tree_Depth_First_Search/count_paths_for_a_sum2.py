class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, target_sum):
    # A map that stores the number of times a prefix sum has occurred so far.
    map = {}

    return count_paths_prefix_sum(root, target_sum, map, 0)


def count_paths_prefix_sum(current_node, target_sum, map, current_path_sum):
    if current_node is None:
        return 0

    # The number of paths that have the required sum.
    path_count = 0

    # 'current_path_sum' is the prefix sum, i.e., sum of all node values from root to current node.
    current_path_sum += current_node.val

    # This is the base case. If the current sum is equal to the target sum, we have found a path from root to
    # the current node having the required sum. Hence, we increment the path count by 1.
    if target_sum == current_path_sum:
        path_count += 1

    # 'current_path_sum' is the path sum from root to the current node. If within this path, there is a
    # valid solution, then there must be an 'old_path_sum' such that:
    # => current_path_sum - old_path_sum = target_sum
    # => current_path_sum - target_sum = old_path_sum
    # Hence, we can search such an 'old_path_sum' in the map from the key 'current_path_sum - target_sum'.
    path_count += map.get(current_path_sum - target_sum, 0)

    # This is the key step in the algorithm. We are storing the number of times the prefix sum
    # `current_path_sum` has occurred so far.
    map[current_path_sum] = map.get(current_path_sum, 0) + 1

    # Counting the number of paths from the left and right subtrees.
    path_count += count_paths_prefix_sum(current_node.left, target_sum, map, current_path_sum)
    path_count += count_paths_prefix_sum(current_node.right, target_sum, map, current_path_sum)

    # Removing the current path sum from the map for backtracking.
    # 'current_path_sum' is the prefix sum up to the current node. When we go back (i.e., backtrack), then
    # the current node is no more a part of the path, hence, we should remove its prefix sum from the map.
    map[current_path_sum] = map.get(current_path_sum, 1) - 1

    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()