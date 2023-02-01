class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        for i in range((len(num)+1)//2):
            if num[i] not in d or d[num[i]] != num[len(num)-1-i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isStrobogrammatic('69'))
    print(s.isStrobogrammatic('88'))
    print(s.isStrobogrammatic('962'))
    print(s.isStrobogrammatic('1'))
