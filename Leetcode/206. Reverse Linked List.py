# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current_node = head
        while(current_node is not None):
            next = current_node.next
            #curent_node = prev
            #current_node = prev
            current_node.next = prev
            prev = current_node
            current_node = next
            
        return prev


        