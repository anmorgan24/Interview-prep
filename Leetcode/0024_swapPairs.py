# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        current, previous = head, None
        while current is not None:
            last_node_of_previous_part = previous
            last_node_of_sub_list = current
            next = None
            
            i = 0
            while current is not None and i < 2:
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1
                
            if last_node_of_previous_part is not None:
                last_node_of_previous_part.next = previous
            else:
                head = previous
                
            last_node_of_sub_list.next = current
            
            if current is None:
                break
            previous = last_node_of_sub_list
                
        return head