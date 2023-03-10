from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
    print(obj.maxProfit([1, 2, 3, 4, 5]))
    print(obj.maxProfit([7, 6, 4, 3, 1]))
    print(obj.maxProfit([1, 2, 3, 0, 2]))
