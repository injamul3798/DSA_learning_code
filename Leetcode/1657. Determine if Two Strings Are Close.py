class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) != len(word2):
            return False

        hash_map_for_word1 = {}
        hash_map_for_word2 = {}

        for st in word1:
            if st in hash_map_for_word1:
                hash_map_for_word1[st] += 1
            else:
                hash_map_for_word1[st] = 1

        for st in word2:
            if st in hash_map_for_word2:
                hash_map_for_word2[st] += 1
            else:
                hash_map_for_word2[st] = 1
        
        # Check if both words contain the same unique characters
        if set(hash_map_for_word1.keys()) != set(hash_map_for_word2.keys()):
            return False

        # Compare the sorted frequency counts
        num1 = sorted(hash_map_for_word1.values())
        num2 = sorted(hash_map_for_word2.values())

        return num1 == num2
