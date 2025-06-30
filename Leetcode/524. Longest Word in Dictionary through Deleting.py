class Solution(object):
    def findLongestWord(self, s, dic):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        ans = ""
        def is_longest(word):
            i = 0
            for st in s:
                if i< len(word) and word[i] == st:
                    i += 1
            return len(word) == i

        for word in dic:
            if is_longest(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                  ans = word    
        return ans
        
