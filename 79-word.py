from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            res = dfs(board, i + 1, j, word[1:]) or dfs(board, i - 1, j, word[1:]) or dfs(
                board, i, j + 1, word[1:]) or dfs(board, i, j - 1, word[1:])
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"
    print(solution.exist(board1, word1))
    print(solution.exist(board1, word2))
    print(solution.exist(board1, word3))
    board2 = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
        "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
    word4 = "AAAAAAAAAAAAA"
    word5 = "AAAAAAAAAAAAAB"
    print(solution.exist(board2, word4))
    print(solution.exist(board2, word5))
