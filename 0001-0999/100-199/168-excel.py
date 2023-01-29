class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            ans = chr(ord('A') + (columnNumber - 1) % 26) + ans
            columnNumber = (columnNumber - 1) // 26
        return ans


if __name__ == '__main__':
    print(Solution().convertToTitle(1))
    print(Solution().convertToTitle(28))
    print(Solution().convertToTitle(701))
    print(Solution().convertToTitle(2147483647))
