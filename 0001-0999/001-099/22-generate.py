from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens += p,
            return parens
        return generate('', n, n)


if __name__ == "__main__":
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(2))
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))
