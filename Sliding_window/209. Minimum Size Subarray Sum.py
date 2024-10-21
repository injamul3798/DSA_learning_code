class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        mn = float('inf')
        left = 0
        c_sum = 0
        for item  in range(len(nums)):
            c_sum += nums[item]
            while(c_sum>= target):
                mn = min(mn,item-left + 1)
                c_sum -= nums[left]
                left += 1

        if mn != float('inf'):
            return mn
        else:
            return 0
            