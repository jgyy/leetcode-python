from typing import List


class Vector2D:
    # Your Vector2D object will be instantiated and called as such:
    # obj = Vector2D(vec)
    # param_1 = obj.next()
    # param_2 = obj.hasNext()
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.pos = 0
        self.size = len(vec)

    def next(self) -> int:
        while self.pos < self.size and not self.vec[self.pos]:
            self.pos += 1
        if self.pos == self.size:
            return None
        return self.vec[self.pos].pop(0)

    def hasNext(self) -> bool:
        while self.pos < self.size and not self.vec[self.pos]:
            self.pos += 1
        return self.pos < self.size


if __name__ == '__main__':
    vec = [[1, 2], [3], [4, 5, 6]]
    v = Vector2D(vec)
    print(v.next())
    print(v.hasNext())
    print(v.next())
    print(v.hasNext())
    print(v.next())
    print(v.hasNext())
    print(v.next())
    print(v.hasNext())
