class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = {}
        for i in strs:
            key = ''.join(sorted(i)) # a e t 
            if key in hash_map:
                hash_map[key].append(i)
            else:
                hash_map[key] = [i]
        return list(hash_map.values())