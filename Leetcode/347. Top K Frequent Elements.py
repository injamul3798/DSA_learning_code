class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        sorted_hash_map = sorted(hash_map.items(),key = lambda x:x[1],reverse = True)
        for i in range(k):
            res.append(sorted_hash_map[i][0])
        
        return res
        
