def rangeSumBST(root, low, high):
	node = root
	if not root:
		return 0

	queue = [(node)]
	running_sum = 0 

	while queue:
		node = queue.pop(0)
		if low <= node.val <=high:
			running_sum+=node.val
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	return running_sum