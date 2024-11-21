class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        window = set()
        sum = 0
        mx = 0
        
        for right in range(len(nums)):
            
            while nums[right] in window:
                window.remove(nums[left])
                sum -= nums[left]
                left += 1
            
            # Add the current element to the window
            window.add(nums[right])
            sum += nums[right]
            
           
            if len(window) == k:
                mx = max(mx, sum)
                window.remove(nums[left])
                sum -= nums[left]
                left += 1
        
        return mx
