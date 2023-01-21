from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, index, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                dfs(candidates, target -
                    candidates[i], i + 1, path + [candidates[i]], res)

        candidates.sort()
        res = []
        dfs(candidates, target, 0, [], res)
        return res


if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
