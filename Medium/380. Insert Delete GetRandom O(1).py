class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []


    def insert(self, val: int) -> bool:
        result = val not in self.numMap

        if result:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)

        return result

    def remove(self, val: int) -> bool:
        result = val in self.numMap

        if result:
            valIndex = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[valIndex] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = valIndex
            del self.numMap[val]
        return result


    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
