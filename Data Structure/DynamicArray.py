class DynamicArray:
    def __init__(self):
        self.array = [0] * 2
        self.currentIndex = 0
        self.capacity = 2

    def add(self,item):
        if (self.currentIndex == self.capacity):
            self.resizeArray()
        self.array[self.currentIndex] = item
        self.currentIndex += 1

    def remove(self):
        if (self.currentIndex == 0):
            raise Exception("Cannot Remove from empty list")
        self.currentIndex -= 1

    def resizeArraY(self):
        self.capacity *= 2
        newArr = [0] * self.capacity
        for i in range(self.array):
            newArr[i] = self.array[i]
        self.array = newArr

    def get(self,index):
        if (index < 0 or index >= self.currentIndex):
            raise Exception("Index out of Bounds")
        return self.array[index]

    def size(self):
        return len(self.array)

# interaksi
myArr = DynamicArray()
myArr.add(3)
myArr.add(4)
print(myArr.size())
myArr.remove()
myArr.remove()
print(myArr.size())