class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_maximum_depth(root):
    if root is None:
        return 0

    queue = [(root)]
    maximumTreeDepth = 0
    while queue:
        maximumTreeDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.pop(0)

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return maximumTreeDepth

