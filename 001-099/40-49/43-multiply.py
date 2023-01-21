class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    num1 = "2"
    num2 = "3"
    print(Solution().multiply(num1, num2))
