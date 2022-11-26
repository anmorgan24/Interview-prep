# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        count = 1
        current = head
        while current and current.next:
            count += 1
            current = current.next
        
        i = 1
        node_1, node_2 = head, head
        while node_1 and i < k:
            node_1 = node_1.next
            i += 1
        i = 1
        while node_2 and i < (count - k + 1):
            node_2 = node_2.next
            i += 1
        
        temp = node_1.val
        node_1.val = node_2.val
        node_2.val = temp
        
        return head