class Trie:
    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)
    def __init__(self):
        self.root = {}
        self.end = '#'

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = self.end

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # returns true
    print(trie.search("app"))     # returns false
    print(trie.startsWith("app")) # returns true
    trie.insert("app")
    print(trie.search("app"))     # returns true
