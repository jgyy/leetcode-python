from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums)):
            if i > k:
                return False
            k = max(k, i + nums[i])
        return True


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().canJump(nums))
