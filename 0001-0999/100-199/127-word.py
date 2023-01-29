from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        beginSet = {beginWord}
        endSet = {endWord}
        step = 1
        while beginSet:
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c != word[i]:
                            newWord = word[:i] + c + word[i + 1:]
                            if newWord in endSet:
                                return step + 1
                            if newWord in wordList:
                                wordList.remove(newWord)
                                nextSet.add(newWord)
            step += 1
            beginSet = nextSet
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("a", "c", ["a", "b", "c"]))
    print(s.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"]))
    print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print(s.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog", "cog"]))
    print(s.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog", "cog", "cog"]))
    print(s.ladderLength("red", "tax", [
          "ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
