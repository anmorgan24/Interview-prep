# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        dummy = pre = ListNode(0)
        dummy.next = head
        while current and current.next:
            if current.val == current.next.val:
                while current and current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                pre.next = current
            else:
                pre = pre.next
                current = current.next
        return dummy.next