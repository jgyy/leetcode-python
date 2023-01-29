from collections import OrderedDict
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.remain:
            self.dic.popitem(last=False)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
