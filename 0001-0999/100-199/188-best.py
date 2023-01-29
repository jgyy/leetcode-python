from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if k >= len(prices) // 2:
            return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))
        dp = [[0] * len(prices) for _ in range(k+1)]
        for i in range(1, k+1):
            min_price = prices[0]
            for j in range(1, len(prices)):
                min_price = min(min_price, prices[j] - dp[i-1][j-1])
                dp[i][j] = max(dp[i][j-1], prices[j]-min_price)
        return dp[-1][-1]


if __name__ == '__main__':
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print(Solution().maxProfit(k, prices))
