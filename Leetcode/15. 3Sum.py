class Solution:
    def threeSum(self, nums):
        results = set()  # Use a set to store unique triplets
        dic = {}
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = nums[i] + nums[j]
                temp = -target
                
                if temp in dic:
                    if i == j or j == dic[temp] or i == dic[temp]:
                        continue
                    else:
                        triplet = tuple(sorted([nums[i], nums[j], temp]))
                        results.add(triplet)
                else:
                    dic[nums[j]] = j

        return [list(triplet) for triplet in results]
         