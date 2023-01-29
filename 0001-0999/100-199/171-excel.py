class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum((ord(c) - 64) * 26 ** i for i, c in enumerate(columnTitle[::-1]))


if __name__ == '__main__':
    print(Solution().titleToNumber('A'))
    print(Solution().titleToNumber('AB'))
    print(Solution().titleToNumber('ZY'))
