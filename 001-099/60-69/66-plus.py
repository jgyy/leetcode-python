from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(int(''.join([str(x) for x in digits])) + 1)]


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([0]))
    print(s.plusOne([9, 9, 9]))
