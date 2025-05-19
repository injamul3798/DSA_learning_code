class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 01
        # hash_map = {}
        # for i in range(len(numbers)):
        #     hash_map[numbers[i]] = i
        
        # for i in range(len(numbers)):
        #     need = target - numbers[i]
        #     if need in hash_map and hash_map[need] > i:
        #         return [i+1,hash_map[need]+1]


        # Solutions 02
        left,right = 0,len(nums)-1
        while left <right:
            current = nums[left] + nums[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left+1,right+1]


        
