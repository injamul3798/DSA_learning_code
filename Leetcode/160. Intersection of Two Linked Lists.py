# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        uniqueNode = set()
        nodeA = headA
        while(nodeA is not None):
            uniqueNode.add(nodeA)
            nodeA = nodeA.next
        
        nodeB = headB
        while nodeB is not None:
            if nodeB in uniqueNode:
                return nodeB
            uniqueNode.add(nodeB)
            nodeB = nodeB.next
        return None
            


        
