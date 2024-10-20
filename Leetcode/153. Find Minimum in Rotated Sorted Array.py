class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mn = nums[0]
        for i in range(1,len(nums)):
            mn  = min(mn,nums[i])

        return mn