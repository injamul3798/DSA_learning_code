class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        # both string same length
        if len(word1) == len(word2):
            for i in range(len(word1)):
                ans += word1[i]
                ans += word2[i]
            return ans
        elif len(word1)<len(word2):
            k = 0
            for i in range(len(word1)):
                ans += word1[i]
                ans += word2[i]
            ans += word2[i+1:len(word2)]
            return ans
        elif len(word1)>len(word2):
            k = 0
            for i in range(len(word2)):
                ans += word1[i]
                ans += word2[i]
            ans += word1[i+1:len(word1)]
            return ans
