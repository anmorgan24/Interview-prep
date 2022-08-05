def minDepth(root):
    node = root
    if not root:
        return 0
        
    queue= [(node, 1)]
        
    while queue:
        node, level = queue.pop(0)
            
        if not node.left and not node.right:
            return level
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))