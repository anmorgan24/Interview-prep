class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result
    
    queue = [(root)]
    
    while queue:
        levelSize = len(queue)
        currentLevel=[]
        
        for _ in range(levelSize):
            currentNode = queue.pop(0)
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        
        result.append(sum(currentLevel)/levelSize)
            
    
    return result