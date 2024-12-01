class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(arr)):
            hash_map[arr[i]*2] = i

         
        
        for i in range(len(arr)):
            if arr[i] in hash_map and hash_map[arr[i]] != i:
                return True
        return False
        
