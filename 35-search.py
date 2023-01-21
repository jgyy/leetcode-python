from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


if __name__ == "__main__":
    nums1 = [1, 3, 5, 6]
    nums2 = [1, 3, 5, 6]
    nums3 = [1, 3, 5, 6]
    print(Solution().searchInsert(nums1, 5))
    print(Solution().searchInsert(nums2, 2))
    print(Solution().searchInsert(nums3, 7))
    print(Solution().searchInsert(nums3, 0))
