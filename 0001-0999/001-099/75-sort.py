from typing import List


class Solution:
    nums: List[int]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
        self.nums = nums


if __name__ == '__main__':
    solution = Solution()
    solution.sortColors([2, 0, 2, 1, 1, 0])
    print(solution.nums)
    solution.sortColors([2, 0, 1])
    print(solution.nums)
    solution.sortColors([0])
    print(solution.nums)
    solution.sortColors([1])
    print(solution.nums)
