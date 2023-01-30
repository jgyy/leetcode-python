class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return False
        return self.isHappy(sum([int(i) ** 2 for i in str(n)]))


if __name__ == '__main__':
    n = 19
    print(Solution().isHappy(n))
