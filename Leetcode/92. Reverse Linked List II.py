# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        current =  head

        left_prev = dummy_node

        for _ in range(left-1):
            left_prev = left_prev.next
             
        current = left_prev.next

        sub_list = current
        prev = None
        for _ in range(right-left+1):
            next = current.next
            current.next = prev
            prev = current
            current = next

        left_prev.next = prev
        sub_list.next = current

        return dummy_node.next
        