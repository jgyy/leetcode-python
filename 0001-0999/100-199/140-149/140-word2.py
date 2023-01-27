from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = ['']
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    for word in dp[j]:
                        dp[i].append(word + ' ' + s[j:i] if word else s[j:i])
        return dp[-1]


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, wordDict))

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(Solution().wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
                "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(Solution().wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
                "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
    print(Solution().wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
                "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
    print(Solution().wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
                "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
    print(Solution().wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
                "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
    print(Solution().wordBreak(s, wordDict))
