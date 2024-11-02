class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if(stack and stack[-1]==s[i]):
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)
