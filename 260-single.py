from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        lowbit = xor & (-xor)
        a, b = 0, 0
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(nums))
