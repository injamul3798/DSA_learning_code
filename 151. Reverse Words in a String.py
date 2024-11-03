class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_string = s.split()
        print('final_string',final_string)
        st = final_string[::-1]
        print('st',st)
        return ' '.join(st)