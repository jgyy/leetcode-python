class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(1))
    print(Solution().isPowerOfTwo(16))
    print(Solution().isPowerOfTwo(218))
