class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) if s.split() else 0


if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
