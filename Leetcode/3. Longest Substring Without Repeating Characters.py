class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        mx = float('-inf')
        left = 0
        for i in range(len(s)):
            while(s[i] in result):
                result = result.replace(s[left], '')
                left += 1
            result += s[i]
            mx = max(mx,i-left+1)
        return mx if mx != float('-inf') else 0