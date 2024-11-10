class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Last and first string has most differnce ,so we only use them 
        ans = 0
        strs.sort()
        firstString = strs[0]
        lastString = strs[-1]
        i = 0
        while(i<len(firstString) and i < len(lastString) and firstString[i]==lastString[i]):
            i += 1
        return firstString[0:i] if i!= 0 else ""
        
