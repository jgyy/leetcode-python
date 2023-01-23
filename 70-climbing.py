class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for _ in range(n - 1):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    n = 3
    print(Solution().climbStairs(n))
