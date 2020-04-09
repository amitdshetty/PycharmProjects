class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        low = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                continue
            maxProfit = max(prices[i] - low, maxProfit)
        return maxProfit

prices = [1, 2]
sol = Solution()
print(sol.maxProfit(prices))