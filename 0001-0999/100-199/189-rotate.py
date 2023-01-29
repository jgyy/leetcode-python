from typing import List


class Solution:
    def __init__(self) -> None:
        self.nums = []

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        self.nums = nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    print(solution.nums)
