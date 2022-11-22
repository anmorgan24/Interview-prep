# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous, current, next = None, head, None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous