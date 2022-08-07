class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    if root is None:
        return result
    
    queue = [(root)]
    leftToRight = True

    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range (levelSize):
            currentNode = queue.pop(0)

            # add the node to the current level based on the traverse direction
            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.insert(0, currentNode.val)

            # insert the children of the current node in the queue

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


        result.append(list(currentLevel))
        # reverse the traversal direction
        leftToRight = not leftToRight

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()