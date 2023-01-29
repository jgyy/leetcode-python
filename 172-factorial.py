class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)


if __name__ == '__main__':
    print(Solution().trailingZeroes(3))
    print(Solution().trailingZeroes(5))
    print(Solution().trailingZeroes(0))
    print(Solution().trailingZeroes(30))
