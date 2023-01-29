from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        sub_len = word_len * word_count
        words = [word for word in words]
        words.sort()
        result = []
        for i in range(len(s) - sub_len + 1):
            sub = [s[i + j * word_len: i + (j + 1) * word_len]
                   for j in range(word_count)]
            sub.sort()
            if sub == words:
                result.append(i)
        return result


if __name__ == "__main__":
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    print(Solution().findSubstring(s1, words1))
    print(Solution().findSubstring(s2, words2))
    print(Solution().findSubstring(s3, words3))
