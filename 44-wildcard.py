class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]


if __name__ == "__main__":
    s = "aa"
    p = "a"
    print(Solution().isMatch(s, p))
    s = "aa"
    p = "a*"
    print(Solution().isMatch(s, p))
    s = "ab"
    p = ".*"
    print(Solution().isMatch(s, p))
    s = "aab"
    p = "c*a*b"
    print(Solution().isMatch(s, p))
    s = "mississippi"
    p = "mis*is*p*."
    print(Solution().isMatch(s, p))
    s = "aa"
    p = "*"
    print(Solution().isMatch(s, p))
