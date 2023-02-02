class Solution:
    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n //= p
        return n == 1


if __name__ == '__main__':
    n1 = 6
    print(Solution().isUgly(n1))
    n2 = 8
    print(Solution().isUgly(n2))
    n3 = 14
    print(Solution().isUgly(n3))
