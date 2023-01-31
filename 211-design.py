from collections import defaultdict


class WordDictionary:
    # Your WordDictionary object will be instantiated and called as such:
    # obj = WordDictionary()
    # obj.addWord(word)
    # param_2 = obj.search(word)
    def __init__(self):
        self.d = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.d[len(word)]
        else:
            for w in self.d[len(word)]:
                for i, char in enumerate(word):
                    if char != '.' and char != w[i]:
                        break
                else:
                    return True
            return False


if __name__ == '__main__':
    trie = WordDictionary()
    trie.addWord("apple")
    print(trie.search("apple"))   # returns true
    print(trie.search("app"))     # returns false
    print(trie.search("app"))  # returns true
    trie.addWord("app")
    print(trie.search("app"))     # returns true
