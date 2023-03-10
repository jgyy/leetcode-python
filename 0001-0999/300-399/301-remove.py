from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses("()())()"))
    print(s.removeInvalidParentheses("(a)())()"))
    print(s.removeInvalidParentheses(")("))
