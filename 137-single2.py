from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += (num >> i) & 1
            result |= (sum % 3) << i
        return result - 2 ** 32 if result > 2 ** 31 - 1 else result


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))
