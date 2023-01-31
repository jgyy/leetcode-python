from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_simple(nums: List[int]) -> int:
            t1 = 0
            t2 = 0
            for current in nums:
                temp = t1
                t1 = max(current + t2, t1)
                t2 = temp

            return t1

        return max(rob_simple(nums[:-1]), rob_simple(nums[1:]))


if __name__ == "__main__":
    print(Solution().rob([2, 7, 9, 3, 1]))
    print(Solution().rob([2, 3, 2]))
