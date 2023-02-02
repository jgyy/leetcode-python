from typing import List


class Solution:
    def __init__(self) -> None:
        self.rooms = None

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2**31-1:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))
        self.rooms = rooms


if __name__ == '__main__':
    rooms = [
        [2**31-1, -1, 0, 2**31-1],
        [2**31-1, 2**31-1, 2**31-1, -1],
        [2**31-1, -1, 2**31-1, -1],
        [0, -1, 2**31-1, 2**31-1]
    ]
    Solution().wallsAndGates(rooms)
    print(rooms)
