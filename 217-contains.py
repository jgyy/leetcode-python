from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))
    print(s.containsDuplicate([1, 2, 3, 4]))
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
