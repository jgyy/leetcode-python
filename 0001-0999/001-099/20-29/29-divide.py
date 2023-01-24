class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(31, -1, -1):
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res


if __name__ == "__main__":
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))
    print(Solution().divide(0, 1))
    print(Solution().divide(1, 1))
    print(Solution().divide(2 ** 31 - 1, 1))
    print(Solution().divide(-2 ** 31, 1))
    print(Solution().divide(-2 ** 31, -1))
