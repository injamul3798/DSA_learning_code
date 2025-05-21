class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 3,5,2,3
        # 2 3 3 5

        # 3,5,4,2,4,6
        # 2 3 4 4 5 6
        # 8 ,8,8
        # Time complexity  = nlogn
        # Space complexity = O(n)
        nums.sort()
        mx = 0
        left,right = 0,len(nums)-1
        while left<=right:
            curr = nums[left] + nums[right]
            if curr>mx:
                mx = curr
            left += 1
            right -= 1
        return mx

