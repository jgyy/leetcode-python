class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        dic = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]] = words[i]
            else:
                if dic[pattern[i]] != words[i]:
                    return False
        return len(set(dic.values())) == len(dic.values())


if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))
    print(s.wordPattern("abba", "dog cat cat fish"))
    print(s.wordPattern("aaaa", "dog cat cat dog"))
    print(s.wordPattern("abba", "dog dog dog dog"))
