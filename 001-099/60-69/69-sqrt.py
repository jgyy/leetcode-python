class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)


if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))
