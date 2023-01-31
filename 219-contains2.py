from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
