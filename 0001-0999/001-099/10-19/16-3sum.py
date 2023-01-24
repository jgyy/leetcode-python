from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return result
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([1, 1, 1, 0], 100))
