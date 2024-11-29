class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        zero_count = 0
        one_count = 0
        two_count = 0

        for key,value in hash_map.items():
            if key == 0:
                zero_count = value
            elif key == 1:
                one_count = value
            else:
                two_count = value
        k = 0
        for _ in range(zero_count):
            nums[k] = 0
            k += 1

         
        for _ in range(k,k+one_count):
            nums[k] = 1
            k += 1

        for _ in range(k,k+two_count):
            nums[k] = 2
            k += 1
            
        
