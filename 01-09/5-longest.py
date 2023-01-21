class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            for i in range(len(s), 0, -1):
                for j in range(len(s) - i + 1):
                    if s[j:j + i] == s[j:j + i][::-1]:
                        return s[j:j + i]


if __name__ == '__main__':
    s = 'babad'
    print(Solution().longestPalindrome(s))
    s = 'cbbd'
    print(Solution().longestPalindrome(s))

    s = 'a'
    print(Solution().longestPalindrome(s))

    s = 'ac'
    print(Solution().longestPalindrome(s))

    s = 'bb'
    print(Solution().longestPalindrome(s))

    s = 'ccc'
    print(Solution().longestPalindrome(s))

    s = 'aaaa'
    print(Solution().longestPalindrome(s))

    s = 'aaaaa'
    print(Solution().longestPalindrome(s))

    s = 'aaaaaa'
    print(Solution().longestPalindrome(s))

    s = 'aaaaaaa'
    print(Solution().longestPalindrome(s))

    s = 'aaaaaaaa'
    print(Solution().longestPalindrome(s))
