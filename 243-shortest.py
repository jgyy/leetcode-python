from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        i1, i2 = -1, -1
        ans = n
        for i in range(n):
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1-i2))
        return ans


if __name__ == '__main__':
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(Solution().shortestDistance(wordsDict, word1, word2))
    word1 = "makes"
    word2 = "coding"
    print(Solution().shortestDistance(wordsDict, word1, word2))
