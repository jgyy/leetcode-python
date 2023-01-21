from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, index, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(candidates, target -
                    candidates[i], i, path + [candidates[i]], res)

        res = []
        dfs(candidates, target, 0, [], res)
        return res


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))
