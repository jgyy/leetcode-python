class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        res = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if len(set(s[i:j + 1])) > 2:
                    break
                res = max(res, j - i + 1)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
    print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
    assert Solution().lengthOfLongestSubstringTwoDistinct("eceba") == 3
    assert Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5
