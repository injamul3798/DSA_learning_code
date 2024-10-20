class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mx = mn = res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <0:
                mx,mn = mn,mx
            mx = max(nums[i],nums[i]*mx)
            mn = min(nums[i],nums[i]*mn)

            res = max(res,mx)

        return res

        