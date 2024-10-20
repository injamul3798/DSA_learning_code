class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mn = float('inf')

        for price in prices:
            mn = min(mn,price) 
            if price > mn:  
               mx = max(mx,price-mn)  
        return mx
