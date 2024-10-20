class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1]*n
        right = [1]*n
        ans = [1]*n

        left[0] = 1
        right[len(nums)-1] = 1

        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]

        ans = []
        for i in range(len(nums)):
            ans.append(left[i]*right[i])

        return ans