from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 3, 1]))
    print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
    assert Solution().findPeakElement([1, 2, 3, 1]) == 2
    assert Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
