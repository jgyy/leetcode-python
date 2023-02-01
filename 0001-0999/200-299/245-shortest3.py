from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = idx2 = -1
        res = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                idx1 = i
            if wordsDict[i] == word2:
                if word1 == word2:
                    idx1 = idx2
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1 - idx2))
        return res


if __name__ == '__main__':
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(Solution().shortestWordDistance(wordsDict, word1, word2))
    word1 = "makes"
    word2 = "coding"
    print(Solution().shortestWordDistance(wordsDict, word1, word2))
    print(Solution().shortestWordDistance(wordsDict, word1, word1))
