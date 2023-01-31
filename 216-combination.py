from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(k, n, start, path, res):
            if k == 0 and n == 0:
                res.append(path)
            for i in range(start, 10):
                if i > n:
                    break
                dfs(k - 1, n - i, i + 1, path + [i], res)

        res = []
        dfs(k, n, 1, [], res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
