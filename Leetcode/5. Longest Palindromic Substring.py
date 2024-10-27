class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_substring = ''
        mx = float('-inf')
        for i in range(len(s)):
            # odd case
            left = i
            right = i
            cnt = 1
            while(left>=0 and right < len(s) and s[left] == s[right]):
                if cnt > mx:
                    mx = cnt
                    longest_substring = s[left:right+1]
                left -= 1
                right += 1
                cnt += 2
            
            #odd case
            left = i
            right = i+1
            cnt = 2
            while(left>=0 and right < len(s) and s[left] == s[right]):
                if cnt > mx:
                    mx = cnt
                    longest_substring = s[left:right+1]
                left -= 1
                right += 1
                cnt += 2

        return longest_substring 
