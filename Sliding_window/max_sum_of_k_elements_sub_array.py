class Solution:
    def max_sum_of_subarray_of_k_elements(self,nums,k):
        pass
        initial_sum = sum(nums[:k])
        #results = []
        #results.append(initial_sum)
        mx = float('-inf')
        for i in range(len(nums)-k):
            initial_sum = initial_sum - nums[i] + nums[i+k]
            #results.append(initial_sum)
            mx = max(mx,initial_sum)
        #return results
        return mx
    
test = Solution()
nums1 = [1, 2, 3, 4, 5, 6]
k1 = 3
print("Test Case 1 Output:", test.max_sum_of_subarray_of_k_elements(nums1, k1))   
 
nums2 = [5, 5, 5, 5, 5]
k2 = 2
print("Test Case 2 Output:", test.max_sum_of_subarray_of_k_elements(nums2, k2))
            
            