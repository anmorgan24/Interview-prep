# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k <= 0:
            return head
        
        last_node = head
        list_length = 1
        while last_node.next is not None:
            last_node = last_node.next
            list_length += 1
            
        last_node.next = head
        k %= list_length
        skip_length = list_length - k
        last_node_of_rotated_list = head
        for i in range(skip_length - 1):
            last_node_of_rotated_list = last_node_of_rotated_list.next
            
        head = last_node_of_rotated_list.next
        last_node_of_rotated_list.next = None
        return head