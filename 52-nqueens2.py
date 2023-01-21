class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            if row == n:
                res.append(["." * i + "Q" + "." * (n - i - 1) for i in queens])
                return
            for col in range(n):
                if col not in queens and row + col not in xy_sum and row - col not in xy_diff:
                    queens.append(col)
                    xy_sum.append(row + col)
                    xy_diff.append(row - col)
                    backtrack(row + 1)
                    queens.pop()
                    xy_sum.pop()
                    xy_diff.pop()

        res = []
        queens = []
        xy_sum = []
        xy_diff = []
        backtrack(0)
        return len(res)


if __name__ == "__main__":
    print(Solution().totalNQueens(4))
    print(Solution().totalNQueens(8))
