class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        p_to_s = {}
        s_to_p = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for p_ch,s_ch in zip(pattern,s):
            if p_ch in p_to_s:
                if p_to_s[p_ch] != s_ch:
                    return False
            else:
                p_to_s[p_ch] = s_ch

            if s_ch in s_to_p:
                if s_to_p[s_ch] != p_ch:
                   return False
            else:
                s_to_p[s_ch] = p_ch
        return True
