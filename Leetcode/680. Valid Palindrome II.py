import re
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        def checkPalindrome(s,left,right):
            while(left<=right):
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s)-1

        while(left<=right):
            if s[left] != s[right]:
                return checkPalindrome(s,left+1,right) or checkPalindrome(s,left,right-1)
            left += 1
            right -= 1
        return True