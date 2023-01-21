class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i, j):
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    f[i][j] |= f[i][j - 2]
                    if match(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if match(i, j):
                        f[i][j] |= f[i - 1][j - 1]

        return f[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("aab", "c*a*b"))
    print(s.isMatch("mississippi", "mis*is*p*."))
    print(s.isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"))
