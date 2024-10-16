class Solution:
    def findMinDifference(self, arr: list[int], m: int) -> int:
        # Sort the array
        arr.sort()
        # Initialize minimum difference as infinity
        mn = float('inf')
        
        # Iterate through the array to find the minimum difference
        for i in range(len(arr) - m + 1):
            mn = min(mn, arr[i + m - 1] - arr[i])
        
        # Return the minimum difference
        return mn
