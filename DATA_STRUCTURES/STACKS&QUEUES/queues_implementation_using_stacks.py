class QueueUsingStack:
    def __init__(self):
        self.first = []
        self.last = []

    def enqueue(self, value):
        for i in range(len(self.first)):
            self.last.append(self.first.pop())

        self.last.append(value)
        return self.last
    
    def dequeue(self):
        for i in range(len(self.last)):
            self.first.append(self.last.pop())
        
        self.first.pop()
        return self.first
    
    def peek(self):
        if len(self.first) > 0:
            return self.first[-1]
        
        if len(self.last) > 0:
            return self.last[0]
        
        return None

myQueue = QueueUsingStack()
print("Enqueue: ")
print(myQueue.enqueue("Microsoft"))
print(myQueue.enqueue("Google"))
print(myQueue.enqueue("Facebook"))
print(myQueue.enqueue("TikTok"))

print("Dequeue: ")
# print(myQueue.dequeue())
# print(myQueue.dequeue())
# print(myQueue.dequeue())
# print(myQueue.dequeue())

print("Peek: ")
print(myQueue.peek())





















"""
class QueueUsingStack:
    def __init__(self):
        self.first = []
        self.last = []

    def enqueue(self, value):
        for i in range(len(self.first)):
            self.last.append(self.first.pop())

        self.last.append(value)
        return self.last

    def dequeue(self):
        for i in range(len(self.last)):
            self.first.append(self.last.pop())

        self.first.pop()
        return self.first
    
    def peek(self):
        if not self.first:
            return None
        
        return self.first[-1]
"""