from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5, 1, 2]))
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
    print(Solution().findMin([11, 13, 15, 17]))
    print(Solution().findMin([1, 3, 5]))
    print(Solution().findMin([2, 2, 2, 0, 1]))
    print(Solution().findMin([1, 3, 3]))
    print(Solution().findMin([3, 3, 1, 3]))
    print(Solution().findMin([10, 1, 10, 10, 10]))
    print(Solution().findMin([1, 3, 5]))
    print(Solution().findMin([2, 2, 2, 0, 1]))
    print(Solution().findMin([1, 3, 3]))
    print(Solution().findMin([3, 3, 1, 3]))
    print(Solution().findMin([10, 1, 10, 10, 10]))
    print(Solution().findMin([1, 3, 5]))
    print(Solution().findMin([2, 2, 2, 0, 1]))
    print(Solution().findMin([1, 3, 3]))
    print(Solution().findMin([3, 3, 1, 3]))
    print(Solution().findMin([10, 1, 10, 10, 10]))
    print(Solution().findMin([1, 3, 5]))
    print(Solution().findMin([2, 2, 2, 0, 1]))
    print(Solution().findMin([1, 3, 3]))
    print(Solution().findMin([3, 3, 1, 3]))
    print(Solution().findMin([10, 1, 10, 10, 10]))
    print(Solution().findMin([1, 3, 5]))
    print(Solution().findMin([2, 2, 2, 0, 1]))
    print(Solution().findMin([1, 3, 3]))
