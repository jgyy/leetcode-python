from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    print(Solution().removeElement(nums1, 3))
    print(Solution().removeElement(nums2, 2))
