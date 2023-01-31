class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right


if __name__ == '__main__':
    left = 5
    right = 7
    print(Solution().rangeBitwiseAnd(left, right))
