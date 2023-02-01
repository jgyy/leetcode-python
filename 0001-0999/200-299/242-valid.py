class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    s1 = 'anagram'
    t1 = 'nagaram'
    print(Solution().isAnagram(s1, t1))
    s2 = 'rat'
    t2 = 'car'
    print(Solution().isAnagram(s2, t2))
