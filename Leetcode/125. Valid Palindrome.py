import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-z0-9]','',s)

        left = 0
        right = len(s)-1
        cnt = 0
        while(left<=right):
            if s[left] != s[right]:
                cnt  = 1
                break
            left += 1
            right -= 1
        return True if cnt == 0 else False