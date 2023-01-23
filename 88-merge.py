from typing import List


class Solution:
    def __init__(self) -> None:
        self.nums1 = []

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                i += 1
                m += 1
        if j < n:
            nums1[i:] = nums2[j:]
        self.nums1 = nums1


if __name__ == "__main__":
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(s.nums1)
