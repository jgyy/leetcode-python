class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if not s or not s[0].isdigit(): return 0
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        return max(-2**31, min(sign*int(s[:i]), 2**31-1))

if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))
    print(solution.myAtoi("-91283472332"))
