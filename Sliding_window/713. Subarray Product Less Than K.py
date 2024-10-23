class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
      
        c_mul = 1
        cnt = left = 0
        
        for i in range(len(nums)):
            c_mul *= nums[i]
            
            while c_mul >= k and left <= i:
                c_mul /= nums[left]   
                left += 1
                
            cnt += i - left + 1
        
        return cnt

        