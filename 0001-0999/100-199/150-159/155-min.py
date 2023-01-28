# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        self.q.append(val)

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return min(self.q)

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
