from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            return 1 if a + b > b + a else -1 if a + b < b + a else 0

        nums = sorted([str(num) for num in nums],
                      key=cmp_to_key(cmp), reverse=True)
        return ''.join(nums).lstrip('0') or '0'


if __name__ == '__main__':
    print(Solution().largestNumber([10, 2]))
    print(Solution().largestNumber([999999991, 9]))
