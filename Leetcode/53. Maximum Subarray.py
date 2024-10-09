class Solution(object):
    def maxSubArray(self, lis):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_sum = lis[0]
        mx = lis[0]


        for i in range(1,len(lis)):
            if c_sum <0:
                c_sum = lis[i]
            else:
                c_sum = c_sum + lis[i]
                
            mx = max(mx,c_sum)

        return mx
        