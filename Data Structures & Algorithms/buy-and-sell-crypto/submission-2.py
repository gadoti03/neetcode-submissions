class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = 100
        max_gain = 0

        for n in prices:
            if n < min_value:
                min_value = n
            else:
                max_gain = max(max_gain, n-min_value)
        return max_gain


    # Complexity
    # O(n)
    #
    # improvements
    # I used dynamic programming to store the minimum value found until i -> memory: 0(n)
    # -> I can avoid Dynamic Programming