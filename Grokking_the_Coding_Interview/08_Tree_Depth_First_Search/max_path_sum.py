class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def findMaxSum(root):
  allPathsSum = []
  find_paths_recursive(root, [], allPathsSum)
  #return allPaths
  return(max(allPathsSum))


def find_paths_recursive(currentNode, currentPath, allPathsSum):
  if currentNode is None:
    return

  # add the current node to the path
  currentPath.append(currentNode.val)

  # if the current node is a leaf and its value is equal to required_sum, save the current path
  if currentNode.left is None and currentNode.right is None:
    allPathsSum.append(sum(list(currentPath)))

  else:
    # traverse the left sub-tree
    find_paths_recursive(currentNode.left, currentPath, allPathsSum)
    # traverse the right sub-tree
    find_paths_recursive(currentNode.right, currentPath, allPathsSum)

  # remove the current node from the path to backtrack,
  # we need to remove the current node while we are going up the recursive call stack.
  del currentPath[-1]


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print(findMaxSum(root))


main()