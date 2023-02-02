from typing import List


class ValidWordAbbr:
    # Your ValidWordAbbr object will be instantiated and called as such:
    # obj = ValidWordAbbr(dictionary)
    # param_1 = obj.isUnique(word)
    def __init__(self, dictionary: List[str]):
        self.dic = {}
        for word in dictionary:
            if len(word) <= 2:
                abbr = word
            else:
                abbr = word[0] + str(len(word)-2) + word[-1]
            if abbr not in self.dic:
                self.dic[abbr] = word
            elif self.dic[abbr] != word:
                self.dic[abbr] = ""

    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            abbr = word
        else:
            abbr = word[0] + str(len(word)-2) + word[-1]
        if abbr not in self.dic:
            return True
        elif self.dic[abbr] == word:
            return True
        else:
            return False


if __name__ == '__main__':
    # Your ValidWordAbbr object will be instantiated and called as such:
    dictionary = ["deer", "door", "cake", "card"]
    obj = ValidWordAbbr(dictionary)
    print(obj.isUnique("dear"))
    print(obj.isUnique("cart"))
    print(obj.isUnique("cane"))
    print(obj.isUnique("make"))
