from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [0, 0]
    nums2 = [0, 0]
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = []
    nums2 = [1]
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [2]
    nums2 = []
    print(Solution().findMedianSortedArrays(nums1, nums2))
