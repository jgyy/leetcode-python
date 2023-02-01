from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        d = {}
        for i, num in enumerate(nums):
            if i > indexDiff:
                d.pop(nums[i - indexDiff - 1] // (valueDiff + 1))
            if num // (valueDiff + 1) in d:
                return True
            if num // (valueDiff + 1) - 1 in d and abs(num - d[num // (valueDiff + 1) - 1]) <= valueDiff:
                return True
            if num // (valueDiff + 1) + 1 in d and abs(num - d[num // (valueDiff + 1) + 1]) <= valueDiff:
                return True
            d[num // (valueDiff + 1)] = num
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
    print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1, 2, 3], 2, 3))
    print(s.containsNearbyAlmostDuplicate([8, 7, 15, 1, 6, 1, 9, 15], 1, 3))
