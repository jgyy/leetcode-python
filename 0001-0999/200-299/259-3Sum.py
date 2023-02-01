from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res


if __name__ == '__main__':
    nums = [-2, 0, 1, 3]
    target = 2
    print(Solution().threeSumSmaller(nums, target))
