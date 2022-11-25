# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1 or head is None:
            return head
        
        current, previous = head, None
        
        count = 1
        while current and current.next:
            count += 1
            current = current.next
            
        current, previous = head, None
        
        while True:
            last_node_of_previous_part = previous
            last_node_of_sub_list = current
            next = None
            i = 0
            while current is not None and i < k:
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
            
            count-=k
            if current is None or count < k:
                break
            previous = last_node_of_sub_list
            
        
        return head