class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans = []
        for candie in candies:
            if candie + extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
