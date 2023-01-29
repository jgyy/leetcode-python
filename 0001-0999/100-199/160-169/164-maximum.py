from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        return max([nums[i] - nums[i - 1] for i in range(1, len(nums))] or [0])


if __name__ == '__main__':
    print(Solution().maximumGap([3, 6, 9, 1]))
    print(Solution().maximumGap([10]))
    assert Solution().maximumGap([3, 6, 9, 1]) == 3
    assert Solution().maximumGap([10]) == 0
