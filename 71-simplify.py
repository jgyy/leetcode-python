class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath('/home/'))
    print(s.simplifyPath('/../'))
    print(s.simplifyPath('/home//foo/'))
    print(s.simplifyPath('/a/./b/../../c/'))
    print(s.simplifyPath('/a/../../b/../c//.//'))
    print(s.simplifyPath('/a//b////c/d//././/..'))
