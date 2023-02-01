from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, start):
            res = []
            for i in range(start, int(n ** 0.5) + 1):
                if n % i == 0:
                    res.append([i, n // i])
                    res += [[i] + r for r in dfs(n // i, i)]
            return res
        return dfs(n, 2)


if __name__ == '__main__':
    n = 32
    print(Solution().getFactors(n))
