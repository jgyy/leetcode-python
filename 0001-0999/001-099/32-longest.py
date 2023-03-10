class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans


if __name__ == "__main__":
    s1 = "(()"
    s2 = ")()())"
    s3 = ""
    print(Solution().longestValidParentheses(s1))
    print(Solution().longestValidParentheses(s2))
    print(Solution().longestValidParentheses(s3))
