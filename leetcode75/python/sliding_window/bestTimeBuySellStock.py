class Solution(object):
    def maxProfit(self, prices: [int]) -> int:
        l = 0
        r = 1

        maxProfit = 0
        while l < r and r < len(prices):
            if prices[r] - prices[l] > maxProfit:
                maxProfit = prices[r] - prices[l]

            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        
        return maxProfit

