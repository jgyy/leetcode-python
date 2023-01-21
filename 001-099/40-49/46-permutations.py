from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        res = []
        dfs(nums, [], res)
        return res


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
    print(Solution().permute([0, 1]))
    print(Solution().permute([1]))
