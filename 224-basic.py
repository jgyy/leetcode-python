class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0  # For the on-going result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)

            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif ch == ')':
                res += sign * operand
                res *= stack.pop()  # stack pop 1, sign
                res += stack.pop()  # stack pop 2, operand
                operand = 0

        return res + sign * operand


if __name__ == '__main__':
    s = Solution()
    print(s.calculate("3+2*2"))
    print(s.calculate(" 3/2 "))
    print(s.calculate(" 3+5 / 2 "))
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
