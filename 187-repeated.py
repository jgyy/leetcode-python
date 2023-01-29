from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s)-9):
            d[s[i:i+10]] = d.get(s[i:i+10], 0) + 1
        return [k for k, v in d.items() if v > 1]


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))
