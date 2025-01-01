from inspect import stack


class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None

class Stack:
    def __init__(self):
        self.arr = []

    def peek(self):
        if len(self.arr) == 0:
            return None
        
        return self.arr[len(self.arr) - 1]

    def push(self, value):
        self.arr.append(value)
        return self.printStack()

    def pop(self):
        if not self.arr:
            return None
        
        self.arr.pop()
        return self.printStack()

    def printStack(self):
        stack_arr = []
        for i in range(len(self.arr)):
            stack_arr.append(self.arr[i])

        return stack_arr


myStack = Stack()
print("Peek: ")
print(myStack.peek())

print("Push: ")
print(myStack.push("microsoft"))
print(myStack.push("google"))
print(myStack.push("facebook"))
print(myStack.push("apple"))

print("Peek: ")
print(myStack.peek())

print("Pop: ")
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())