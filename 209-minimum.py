from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        min_len = len(nums) + 1
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if min_len == len(nums) + 1 else min_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(sol.minSubArrayLen(4, [1, 4, 4]))
    print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
