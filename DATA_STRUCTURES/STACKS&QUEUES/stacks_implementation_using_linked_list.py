from inspect import stack


class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return None
        
        return self.top

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.top = node
            self.bottom = self.top
            self.length += 1
            return self.printStack()
        
        holdingPointer = self.top
        self.top = node
        self.top.next = holdingPointer
        self.length += 1

        return self.printStack()

    def pop(self):
        if not self.top:
            return None
        
        if self.top == self.bottom:
            self.bottom = None
             
        self.top = self.top.next
        self.length -= 1
        return self.printStack()

    def printStack(self):
        stack_arr = []
        currentNode = self.top
        while currentNode != None:
            stack_arr.append(currentNode.value)
            currentNode = currentNode.next

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
print(myStack.peek().value)

print("Pop: ")
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())