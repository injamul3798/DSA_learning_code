from collections import deque
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = deque()
        left,right = 0,len(nums)-1
        while(left<=right):
             
            if abs(nums[left])>abs(nums[right]):
                ans.appendleft(nums[left]*nums[left])
                left += 1
            else:
                ans.appendleft(nums[right]*nums[right])
                right -= 1
        return list(ans)
