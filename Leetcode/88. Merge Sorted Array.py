class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n -1
        k = m + n -1
        while(right>=0):
            if left >=0 and nums1[left] > nums2[right]:
                nums1[k] = nums1[left]
                left -= 1
            else:
                nums1[k] = nums2[right]
                right -= 1
            k -= 1
        

        
