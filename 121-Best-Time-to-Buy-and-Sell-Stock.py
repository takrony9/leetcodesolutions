class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,buy = 0,prices[0]
        for price in prices:
                buy = min(price,buy)
                profit = max(price-buy,profit)   
        return profit                  