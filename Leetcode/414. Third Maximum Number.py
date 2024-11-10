class Solution:
    def thirdMax(self, nums):
        first = second = third = float('-inf')
        
        for num in nums:
            # Skip duplicates
            if num == first or num == second or num == third:
                continue
            if num> first:
                third  = second
                second  = first
                first  = num
            elif num >second:
                third = second
                second  = num

            elif num >third:
                third = num
        
        # Return third if it was updated; otherwise, return first
        return third if third != float('-inf') else first
