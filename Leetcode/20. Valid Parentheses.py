class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for st in s:
            if st in '({[':
                stack.append(st)
            elif st in ')}]':
                if not stack:
                    return False
                else:
                    if st == ')':
                        if stack[-1]=='(':
                            stack.pop()
                        else:
                            return False
                    elif st == '}':
                        if stack[-1]=='{':
                            stack.pop()
                        else:
                            return False
                    elif st == ']':
                        if stack[-1]=='[':
                            stack.pop()
                        else:
                            return False

        return len(stack)==0