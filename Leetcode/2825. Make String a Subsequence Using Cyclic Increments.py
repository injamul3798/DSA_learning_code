class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i = j = 0   # take two pointer
        m = len(str1)
        n = len(str2)

        while(i<m and j < n):
            if str1[i] == str2[j]:    # if equal then move to the next one
                i += 1
                j += 1
            elif (str1[i] == 'z' and str2[j] == 'a') or (ord(str1[i])+1 == ord(str2[j])):
                i += 1
                j += 1
            else:
                i += 1
        return j == n

         
