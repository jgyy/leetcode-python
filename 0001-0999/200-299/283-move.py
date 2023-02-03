from typing import List


class Solution:
    def __init__(self) -> None:
        self.nums = None

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        self.nums = nums


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(solution.nums)
    assert solution.nums == [1, 3, 12, 0, 0]
    nums = [0, 0, 0, 0, 0]
    solution.moveZeroes(nums)
    print(solution.nums)
    assert solution.nums == [0, 0, 0, 0, 0]
    nums = [1, 2, 3, 4, 5]
    solution.moveZeroes(nums)
    print(solution.nums)
    assert solution.nums == [1, 2, 3, 4, 5]
    nums = [1, 0, 1]
    solution.moveZeroes(nums)
    print(solution.nums)
    assert solution.nums == [1, 1, 0]
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(solution.nums)
    assert solution.nums == [1, 3, 12, 0, 0]
