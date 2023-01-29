class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        current_row = 0
        going_down = False
        for c in s:
            rows[current_row] += c
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return ''.join(rows)


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    numRows = 3
    print(Solution().convert(s, numRows))
    s = 'PAYPALISHIRING'
    numRows = 4
    print(Solution().convert(s, numRows))

    s = 'A'
    numRows = 1
    print(Solution().convert(s, numRows))

    s = 'AB'
    numRows = 1
    print(Solution().convert(s, numRows))

    s = 'AB'
    numRows = 2
    print(Solution().convert(s, numRows))

    s = 'ABC'
    numRows = 2
    print(Solution().convert(s, numRows))

    s = 'ABCD'
    numRows = 2
    print(Solution().convert(s, numRows))

    s = 'ABCDE'
    numRows = 2
    print(Solution().convert(s, numRows))

    s = 'ABCDE'
    numRows = 3
    print(Solution().convert(s, numRows))

    s = 'ABCDE'
    numRows = 4
    print(Solution().convert(s, numRows))

    s = 'ABCDE'
    numRows = 5
    print(Solution().convert(s, numRows))

    s = 'ABCDE'
    numRows = 6
    print(Solution().convert(s, numRows))
