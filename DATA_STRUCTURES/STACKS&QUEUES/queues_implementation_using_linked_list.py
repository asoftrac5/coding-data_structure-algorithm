class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return None
        return self.first

    def enqueue(self, value):
        node = Node(value)

        if self.length == 0:
            self.first = node
            self.last = self.first
            self.length += 1
            return self.printQueue()

        last = self.last
        last.next = node
        self.last = node
        self.length += 1
        
        return self.printQueue()

    def dequeue(self):
        if self.length == 0:
            return None
        
        if self.first == self.last:
            self.last = None
        
        first = self.first
        self.first = first.next
        self.length -= 1
        return self.printQueue()

    def printQueue(self):
        queue_array = []
        currentNode = self.first
        while currentNode != None:
            queue_array.append(currentNode.value)
            currentNode = currentNode.next

        return queue_array

myQueue = Queue()
print("Peek: ")
print(myQueue.peek())

print("Enqueue: ")
print(myQueue.enqueue("Microsoft"))
print(myQueue.enqueue("Google"))
print(myQueue.enqueue("Facebook"))
print(myQueue.enqueue("Netflix"))
print(myQueue.enqueue("TikTok"))


print("Peek: ")
print(myQueue.peek().value)

print("Dequeue: ")
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())