from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


if __name__ == "__main__":
    nums1 = [-1, 0, 3, 5, 9, 12]
    nums2 = [-1, 0, 3, 5, 9, 12]
    nums3 = [-1, 0, 3, 5, 9, 12]
    print(Solution().search(nums1, 9))
    print(Solution().search(nums2, 2))
    print(Solution().search(nums3, 12))
