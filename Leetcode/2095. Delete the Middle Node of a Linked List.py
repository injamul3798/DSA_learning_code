# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head
        dummy_node = ListNode(0)
        dummy_node.next = head
        
        
        while(fast and fast.next is not None):
            
            fast = fast.next.next
            slow = slow.next
            dummy_node = dummy_node.next
        dummy_node.next = slow.next
        return head
        
