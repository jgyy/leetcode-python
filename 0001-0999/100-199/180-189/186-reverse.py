from typing import List


class Solution:
    def __init__(self) -> None:
        self.s = []

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        i = 0
        for j in range(len(s)):
            if s[j] == ' ':
                s[i:j] = reversed(s[i:j])
                i = j + 1
        s[i:] = reversed(s[i:])
        self.s = s


if __name__ == '__main__':
    s = ["t", "h", "e", " ", "s", "k", "y",
         " ", "i", "s", " ", "b", "l", "u", "e"]
    Solution().reverseWords(s)
    print(s)
