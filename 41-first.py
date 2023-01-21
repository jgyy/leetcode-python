from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 1
        for num in nums:
            if num > 0:
                if i == num:
                    i += 1
                elif i < num:
                    return i
        return i


if __name__ == "__main__":
    nums1 = [1, 2, 0]
    nums2 = [3, 4, -1, 1]
    nums3 = [7, 8, 9, 11, 12]
    print(Solution().firstMissingPositive(nums1))
    print(Solution().firstMissingPositive(nums2))
    print(Solution().firstMissingPositive(nums3))
