from typing import List


class Solution:
    def __init__(self) -> None:
        self.nums = None

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        self.nums = nums


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 5, 2, 1, 6, 4]
    solution.wiggleSort(nums)
    print(solution.nums)
    assert solution.nums == [1, 3, 2, 5, 4, 6]
    nums = [6, 6, 5, 6, 3, 8]
    solution.wiggleSort(nums)
    print(solution.nums)
    assert solution.nums == [3, 6, 5, 6, 6, 8]
