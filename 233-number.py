class Solution:
    def countDigitOne(self, n: int) -> int:
        ones = 0
        m = 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones


if __name__ == '__main__':
    print(Solution().countDigitOne(13))
    print(Solution().countDigitOne(0))
    print(Solution().countDigitOne(1))
    print(Solution().countDigitOne(10))
    print(Solution().countDigitOne(100))
    print(Solution().countDigitOne(1000))
    print(Solution().countDigitOne(10000))
    print(Solution().countDigitOne(100000))
    print(Solution().countDigitOne(1000000))
    print(Solution().countDigitOne(10000000))
    print(Solution().countDigitOne(100000000))
    print(Solution().countDigitOne(1000000000))
    print(Solution().countDigitOne(10000000000))
    print(Solution().countDigitOne(100000000000))
    print(Solution().countDigitOne(1000000000000))
    print(Solution().countDigitOne(10000000000000))
    print(Solution().countDigitOne(100000000000000))
    print(Solution().countDigitOne(1000000000000000))
    print(Solution().countDigitOne(10000000000000000))
    print(Solution().countDigitOne(100000000000000000))
    print(Solution().countDigitOne(1000000000000000000))
    print(Solution().countDigitOne(10000000000000000000))
    print(Solution().countDigitOne(100000000000000000000))
    print(Solution().countDigitOne(1000000000000000000000))
    print(Solution().countDigitOne(10000000000000000000000))
    print(Solution().countDigitOne(100000000000000000000000))
    print(Solution().countDigitOne(1000000000000000000000000))
    print(Solution().countDigitOne(10000000000000000000000000))
    print(Solution().countDigitOne(100000000000000000000000000))
    print(Solution().countDigitOne(1000000000000000000000000000))
    print(Solution().countDigitOne(10000000000000000000000000000))
    print(Solution().countDigitOne(100000000000000000000000000000))
    print(Solution().countDigitOne(1000000000000000000000000000000))
