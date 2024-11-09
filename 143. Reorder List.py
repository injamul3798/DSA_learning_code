# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # Find the mid element
        slow = head
        fast = head
        while(fast and fast.next is not None):
            slow = slow.next
            fast  = fast.next.next

        mid  = slow

        #Reverse the second half
        prev,current = None,slow
        while(current):
            next  = current.next
            current.next = prev
            prev = current
            current = next

        # Join the list
        first,second  = head,prev

        while second.next:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2




        

        
