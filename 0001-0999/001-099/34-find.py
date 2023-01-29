from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left, right = mid, mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
        return [-1, -1]


if __name__ == "__main__":
    nums1 = [5, 7, 7, 8, 8, 10]
    nums2 = [5, 7, 7, 8, 8, 10]
    nums3 = [5, 7, 7, 8, 8, 10]
    print(Solution().searchRange(nums1, 8))
    print(Solution().searchRange(nums2, 6))
    print(Solution().searchRange(nums3, 10))
