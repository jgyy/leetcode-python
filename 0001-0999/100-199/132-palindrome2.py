class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    dp[i] = min(dp[i], dp[j-1]+1 if j > 0 else 0)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minCut('aab'))
