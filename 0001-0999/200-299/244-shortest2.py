from typing import List
from collections import defaultdict


class WordDistance:
    # Your WordDistance object will be instantiated and called as such:
    # obj = WordDistance(wordsDict)
    # param_1 = obj.shortest(word1,word2)
    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]
        i = j = 0
        minDist = float('inf')
        while i < len(loc1) and j < len(loc2):
            minDist = min(minDist, abs(loc1[i] - loc2[j]))
            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1
        return minDist


if __name__ == '__main__':
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    obj = WordDistance(wordsDict)
    print(obj.shortest(word1, word2))
    word1 = "makes"
    word2 = "coding"
    print(obj.shortest(word1, word2))
