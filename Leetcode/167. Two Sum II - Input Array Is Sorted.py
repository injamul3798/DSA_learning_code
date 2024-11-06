class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(numbers)):
            hash_map[numbers[i]] = i

        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in hash_map and hash_map[temp] > i:
                return [i+1,hash_map[temp]+1]

        return -1

        