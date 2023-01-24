from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return length
        i = 2
        for j in range(2, length):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
