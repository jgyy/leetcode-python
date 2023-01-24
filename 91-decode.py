class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1] != '0' and int(s[i - 1: i + 1]) <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('12'))
    print(s.numDecodings('226'))
    print(s.numDecodings('0'))
    print(s.numDecodings('06'))
    print(s.numDecodings('10'))
