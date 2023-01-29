# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
class TwoSum:

    def __init__(self):
        self.nums = []
        self.is_sorted = False

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True
        i, j = 0, len(self.nums) - 1
        while i < j:
            if self.nums[i] + self.nums[j] == value:
                return True
            elif self.nums[i] + self.nums[j] < value:
                i += 1
            else:
                j -= 1
        return False

if __name__ == '__main__':
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    print(obj.find(4))
    print(obj.find(7))
