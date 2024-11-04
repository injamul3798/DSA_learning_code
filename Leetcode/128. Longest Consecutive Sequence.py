class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = set(nums)
        print(st)
        mx = 0
        for num in nums:
            if num-1 not in st:
                cnt = 1
                current = num + 1
                while(current in st):
                    cnt += 1
                    current += 1
                mx = max(mx,cnt)
        return mx