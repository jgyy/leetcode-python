from typing import List


class Solution:
    nums: List[int]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        self.nums = nums


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 1]
    nums3 = [1, 1, 5]
    nums4 = [1]
    s1 = Solution()
    s1.nextPermutation(nums1)
    s2 = Solution()
    s2.nextPermutation(nums2)
    s3 = Solution()
    s3.nextPermutation(nums3)
    s4 = Solution()
    s4.nextPermutation(nums4)
    print(s1.nums)
    print(s2.nums)
    print(s3.nums)
    print(s4.nums)
