class Solution:
    def __init__(self):
        self.scrambles = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.scrambles:
            return self.scrambles[(s1, s2)]
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.scrambles[(s1, s2)] = True
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.scrambles[(s1, s2)] = True
                return True
        self.scrambles[(s1, s2)] = False
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isScramble("great", "rgeat"))
    print(s.isScramble("abcde", "caebd"))
    print(s.isScramble("a", "a"))
    print(s.isScramble("abc", "bca"))
    print(s.isScramble("abc", "cba"))
    print(s.isScramble("abcdefghijklmnopq", "efghijklmnopqcadb"))
    print(s.isScramble("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"))
