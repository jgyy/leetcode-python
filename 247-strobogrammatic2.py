from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
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

        return dfs(n, n)


if __name__ == '__main__':
    s = Solution()
    for i in range(16):
        print(s.findStrobogrammatic(i))
