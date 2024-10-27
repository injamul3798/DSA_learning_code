class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mx = float('-inf')
        cnt = 0
        for i in range(len(s)):
            # odd case
            left = i
            right = i
             
            while(left>=0 and right < len(s) and s[left] == s[right]):   
                left -= 1
                right += 1
                cnt += 1
            
            #odd case
            left = i
            right = i+1
            
            while(left>=0 and right < len(s) and s[left] == s[right]):      
                left -= 1
                right += 1
                cnt += 1

        return cnt 

        