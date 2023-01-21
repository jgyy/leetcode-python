from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        maxPosition = 0
        steps = 0
        for i in range(len(nums) - 1):
            maxPosition = max(maxPosition, i + nums[i])
            if i == end:
                end = maxPosition
                steps += 1
        return steps


if __name__ == "__main__":
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [2, 3, 0, 1, 4]
    print(Solution().jump(nums1))
    print(Solution().jump(nums2))
