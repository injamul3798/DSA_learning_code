# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        def reverse(current):
            prev = None
            while(current):
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        # Got the reverse head
        reverseListHead = reverse(head)

        dummy = ListNode(0)
        dummy.next = reverseListHead

        current  = dummy
        for _ in range(n-1):
            current = current.next
        current.next = current.next.next

        return reverse(dummy.next)

        
