class Solution(object):
    def findDuplicate(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(0,len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1
         
        for key,value in dic.items():
            if value> 1:
                return key

        