# Implement array from the scratch

class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data.get(index)
    
    def append(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    
    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def shiftItems(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
    
newArray = MyArray()
print(newArray.append('hi'))
print(newArray.append('you'))
print(newArray.append('!'))
# newArray.pop()
print(newArray.delete(1))
print(newArray.get(1))
print(newArray.get(2))