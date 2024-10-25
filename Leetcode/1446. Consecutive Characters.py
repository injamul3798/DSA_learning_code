class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = s[0]
        cnt = 1
        mx = float('-inf')
        for i in range(1,len(s)):
            if s[i] == prev:
                cnt += 1
            else:
                prev = s[i]
                cnt = 1
            mx = max(mx,cnt)
        return mx if mx != float('-inf') else 1