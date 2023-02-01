from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(v % 2 for v in Counter(s).values()) < 2


if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome("code"))
    print(s.canPermutePalindrome("aab"))
    print(s.canPermutePalindrome("carerac"))
