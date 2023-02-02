class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        dp = [0] * n
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numWays(3, 2))
    assert Solution().numWays(3, 2) == 6
    print(Solution().numWays(1, 1))
    assert Solution().numWays(1, 1) == 1
    print(Solution().numWays(7, 2))
    assert Solution().numWays(7, 2) == 42
