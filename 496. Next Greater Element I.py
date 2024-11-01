class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        stack = []
        hash_map = {}
        for num in nums2:
            while(stack and stack[-1]<num):
                pop_item = stack.pop()
                hash_map[pop_item] = num
            stack.append(num)
        
        while stack:
             pop_item = stack.pop()
             hash_map[pop_item] = -1
        for num in nums1:
            ans.append(hash_map[num])
        return ans
        