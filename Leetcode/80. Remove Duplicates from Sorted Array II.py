class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if i ==0:
                nums[k] = nums[i]
                k += 1
            else:
                if (i>0 and i <len(nums)-1 and nums[i] == nums[i-1]) and (nums[i]==nums[i+1]):
                    continue
                else:
                    nums[k] = nums[i]
                    k += 1
        return k
