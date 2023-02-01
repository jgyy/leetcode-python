class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def dfs(n, m):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]
            res = []
            for s in dfs(n - 2, m):
                if n != m:
                    res.append("0" + s + "0")
                res.append("1" + s + "1")
                res.append("6" + s + "9")
                res.append("8" + s + "8")
                res.append("9" + s + "6")
            return res

        def check(s):
            return len(s) == len(low) and s < low or \
                len(s) == len(high) and s > high

        res = 0
        for i in range(len(low), len(high) + 1):
            res += sum(1 for s in dfs(i, i) if not check(s))
        return res


if __name__ == '__main__':
    low = "50"
    high = "100"
    print(Solution().strobogrammaticInRange(low, high))
