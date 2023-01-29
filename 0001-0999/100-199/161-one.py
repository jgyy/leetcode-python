class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        if len(s) - len(t) > 1:
            return False
        if len(s) == len(t):
            return sum([s[i] != t[i] for i in range(len(s))]) == 1
        for i in range(len(t)):
            if s[i] != t[i]:
                return s[i + 1:] == t[i:]
        return True

if __name__ == '__main__':
    print(Solution().isOneEditDistance('ab', 'acb'))
    print(Solution().isOneEditDistance('cab', 'ad'))
    print(Solution().isOneEditDistance('1203', '1213'))
    assert Solution().isOneEditDistance('ab', 'acb') == True
    assert Solution().isOneEditDistance('cab', 'ad') == False
    assert Solution().isOneEditDistance('1203', '1213') == True
