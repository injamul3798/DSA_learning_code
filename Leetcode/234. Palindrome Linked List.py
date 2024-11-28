# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None:
            return True
        
        fast = head
        slow = head
        first = head

        while(fast and fast.next is not None):
            fast = fast.next.next
            slow = slow.next

        # reverse the second part
        prev = None
        while(slow):
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # now compare 
        second = prev
        cnt = 0
        while(second):
            if first.val != second.val:
                cnt = 1
                break
            first = first.next
            second = second.next
        if cnt == 1:
            return False
        return True

