class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            another_value = target - nums[i]
            if another_value in dic:
                return [dic[target - nums[i]],i]
            dic[nums[i]] = i