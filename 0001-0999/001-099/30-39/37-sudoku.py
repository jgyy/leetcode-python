from typing import List


class Solution:
    board: List[List[str]]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(r: int, c: int, num: str) -> bool:
            for i in range(9):
                if board[i][c] == num or board[r][i] == num:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(r // 3) * 3 + i][(c // 3) * 3 + j] == num:
                        return False
            return True

        def backtrack(r: int, c: int) -> bool:
            if c == 9:
                return backtrack(r + 1, 0)
            if r == 9:
                return True
            if board[r][c] != '.':
                return backtrack(r, c + 1)
            for num in range(1, 10):
                if isValid(r, c, str(num)):
                    board[r][c] = str(num)
                    if backtrack(r, c + 1):
                        return True
                    board[r][c] = '.'
            return False

        backtrack(0, 0)
        self.board = board


if __name__ == "__main__":
    board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board2 = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
              ["7", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", "2", ".", "1", ".", "9", ".", ".", "."],
              [".", ".", "7", ".", ".", ".", "2", "4", "."],
              [".", "6", "4", ".", "1", ".", "5", "9", "."],
              [".", "9", "8", ".", ".", ".", "3", ".", "."],
              [".", ".", ".", "8", ".", "3", ".", "2", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "6"],
              [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    s1 = Solution()
    s2 = Solution()
    s1.solveSudoku(board1)
    s2.solveSudoku(board2)
    print(s1.board)
    print(s2.board)
