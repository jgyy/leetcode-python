class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ')' and stack.pop() != '(':
                    return False
                if c == ']' and stack.pop() != '[':
                    return False
                if c == '}' and stack.pop() != '{':
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("{[]}"))
