class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


if __name__ == "__main__":
    print(Solution().myPow(2.00000, 10))
    print(Solution().myPow(2.10000, 3))
    print(Solution().myPow(2.00000, -2))
