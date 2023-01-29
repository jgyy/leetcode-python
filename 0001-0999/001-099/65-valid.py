class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s in ['inf', '-inf', '+inf', 'Infinity', '+Infinity', '-Infinity']:
            return False
        try:
            float(s)
            return True
        except:
            return False


if __name__ == '__main__':
    s = Solution()
    for i in ['0', ' 0.1 ', 'abc', '1 a', '2e10', ' -90e3   ',
              ' 1e', 'e3', ' 6e-1', ' 99e2.5 ', '53.5e93', ' --6 ',
              '-+3', '95a54e53', 'inf', 'nan', '2e0']:
        print(s.isNumber(i))
