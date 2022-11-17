# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
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
            return True
        
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        head_second_half = reverse(slow)
        copy_head_second_half = head_second_half
        
        while head is not None and head_second_half is not None:
            if head.val != head_second_half.val:
                break
            head = head.next
            head_second_half = head_second_half.next
        reverse(copy_head_second_half)
        
        if head is None or head_second_half is None:
            return True
        return False