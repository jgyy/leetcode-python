from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for s in strings:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
            d[key] = d.get(key, []) + [s]
        return list(d.values())


if __name__ == '__main__':
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(Solution().groupStrings(strings))
