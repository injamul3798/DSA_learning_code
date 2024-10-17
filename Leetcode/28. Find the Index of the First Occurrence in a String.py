class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        index = haystack.find(needle)
        if index != -1:
            return index
        return -1