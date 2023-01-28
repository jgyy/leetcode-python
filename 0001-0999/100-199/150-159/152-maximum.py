from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_i = min_i = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_i, min_i = min_i, max_i
            max_i = max(nums[i], max_i * nums[i])
            min_i = min(nums[i], min_i * nums[i])
            res = max(res, max_i)
        return res


if __name__ == '__main__':
    print(Solution().maxProduct([3, 4, 5, 2]))
    print(Solution().maxProduct([1, 5, 4, 5]))
    print(Solution().maxProduct([-2, 0, -1]))
    print(Solution().maxProduct([3, 7]))
    assert Solution().maxProduct([3, 4, 5, 2]) == 120
    assert Solution().maxProduct([1, 5, 4, 5]) == 100
    assert Solution().maxProduct([-2, 0, -1]) == 0
    assert Solution().maxProduct([3, 7]) == 21
