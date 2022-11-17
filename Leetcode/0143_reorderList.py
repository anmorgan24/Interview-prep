# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        def reverse(head):
            prev = None
            while head is not None:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        if head is None or head.next is None:
            return
        
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        head_second_half = reverse(slow)
        head_first_half = head
        
        while head_first_half is not None and head_second_half is not None:
            temp = head_first_half.next
            head_first_half.next = head_second_half
            head_first_half = temp
            
            temp = head_second_half.next
            head_second_half.next = head_first_half
            head_second_half = temp
            
        if head_first_half is not None:
            head_first_half.next = None
            