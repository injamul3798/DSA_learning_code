class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_mapA = {}
        hash_mapB = {}

        for ch in ransomNote:
            if ch in hash_mapA:
                hash_mapA[ch] += 1
            else:
                hash_mapA[ch] = 0

        for ch in magazine:
            if ch in hash_mapB:
                hash_mapB[ch] += 1
            else:
                hash_mapB[ch] = 0

        for key,value in hash_mapA.items():
            if key in hash_mapB:
                if hash_mapB[key] >= value:
                    continue
                else:
                    return False
            else:
                return False
        return True
