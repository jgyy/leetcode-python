class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world!  "))
    print(Solution().reverseWords("a good   example"))
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    assert Solution().reverseWords("  hello world!  ") == "world! hello"
    assert Solution().reverseWords("a good   example") == "example good a"
