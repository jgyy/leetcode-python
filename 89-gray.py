from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        return [x for x in self.grayCode(n - 1)] + [x + 2 ** (n - 1) for x in reversed(self.grayCode(n - 1))]


if __name__ == "__main__":
    s = Solution()
    print(s.grayCode(0))
    print(s.grayCode(1))
    print(s.grayCode(2))
    print(s.grayCode(3))
    print(s.grayCode(4))
