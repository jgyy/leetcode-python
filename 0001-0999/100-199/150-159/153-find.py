from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5, 1, 2]))
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
    print(Solution().findMin([11, 13, 15, 17]))
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([11, 13, 15, 17]) == 11
