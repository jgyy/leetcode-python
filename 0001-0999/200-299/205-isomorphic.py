class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]


if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(Solution().isIsomorphic(s, t))
