class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s = s[0] + s[1:][::-1]
        else:
            s = s[::-1]
        if int(s) > 2**31 - 1 or int(s) < -2**31:
            return 0
        else:
            return int(s)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(0))
