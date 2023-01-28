class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        for i in range(max(len(v1), len(v2))):
            a = int(v1[i]) if i < len(v1) else 0
            b = int(v2[i]) if i < len(v2) else 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

if __name__ == '__main__':
    print(Solution().compareVersion('0.1', '1.1'))
    print(Solution().compareVersion('1.0.1', '1'))
