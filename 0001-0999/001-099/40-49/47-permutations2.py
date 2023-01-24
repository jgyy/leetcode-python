from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        nums.sort()
        res = []
        dfs(nums, [], res)
        return res


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
    print(Solution().permuteUnique([1, 2, 3]))
