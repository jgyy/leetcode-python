from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            d[key] = d.get(key, []) + [s]
        return list(d.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["a"]))
