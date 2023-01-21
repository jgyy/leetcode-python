class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    haystack1 = "hello"
    needle1 = "ll"
    haystack2 = "aaaaa"
    needle2 = "bba"
    haystack3 = ""
    needle3 = ""
    print(Solution().strStr(haystack1, needle1))
    print(Solution().strStr(haystack2, needle2))
    print(Solution().strStr(haystack3, needle3))
