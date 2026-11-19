class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [0]*n
        min_value = prices[0]

        for i in range(n):
            min_value = min(min_value, prices[i]) 
            dp[i] = min_value
        
        max_difference = 0
        for i in range(n):
            max_difference = max(max_difference, prices[i] - dp[i])
        return max_difference