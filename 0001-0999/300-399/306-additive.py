class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == "0" and i > 1:
                break
            for j in range(i + 1, n):
                if num[i] == "0" and j > i + 1:
                    break
                x1, x2 = int(num[:i]), int(num[i:j])
                k = j
                while k < n:
                    x3 = x1 + x2
                    if num[k:].startswith(str(x3)):
                        k += len(str(x3))
                        x1, x2 = x2, x3
                    else:
                        break
                if k == n:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("1023"))
    print(s.isAdditiveNumber("0235813"))
    print(s.isAdditiveNumber("101"))
    print(s.isAdditiveNumber("1203"))
    print(s.isAdditiveNumber("121474836472147483648"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("1023"))
    print(s.isAdditiveNumber("0235813"))
    print(s.isAdditiveNumber("101"))
    print(s.isAdditiveNumber("1203"))
    print(s.isAdditiveNumber("121474836472147483648"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("1023"))
    print(s.isAdditiveNumber("0235813"))
    print(s.isAdditiveNumber("101"))
    print(s.isAdditiveNumber("1203"))
    print(s.isAdditiveNumber("121474836472147483648"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("1023"))
    print(s.isAdditiveNumber("0235813"))
    print(s.isAdditiveNumber("101"))
    print(s.isAdditiveNumber("1203"))
    print(s.isAdditiveNumber("121474836472147483648"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("1023"))
    print(s.isAdditiveNumber("0235813"))
    print(s.isAdditiveNumber("101"))
    print(s.isAdditiveNumber("1203"))
    print(s.isAdditiveNumber("121474836472147483648"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
