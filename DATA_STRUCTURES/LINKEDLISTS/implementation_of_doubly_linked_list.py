# <--10 <--> 5 <--> 16 -->

# Structure
# myLinkedList = {
#     "value": 10,
#     "next": {
#         "value": 5,
#         "next": {
#             "value": 16,
#             "next": None
#         },
#         "previous": {
#             "value": 10,
#             "next":
#         }
#     },
# }

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
            self.length += 1
        
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1

            return node.value, node.next, node.previous.value
    
    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.length += 1

            return node.value, node.next.value, node.previous
    
    def insert(self, index, value):
        # check params
        if index >= self.length:
            return self.append(value)
        
        if index < 0:
            return self.prepend(value)

        node = Node(value)
        # *   *
        #  \ /
        #   *
        leader = self.traverseToIndex(index - 1)
        sucessor = leader.next
        leader.next = node
        node.previous = leader
        node.next = sucessor
        sucessor.previous = node
        self.length += 1
        return self.printList()
    
    def remove(self, index):
        # leader = self.traverseToIndex(index - 1)
        # successor = self.traverseToIndex(index + 1)
        # leader.next = successor

        # Or

        node_to_remove = self.traverseToIndex(index)
        predecessor = node_to_remove.previous
        successor = node_to_remove.next
        predecessor.next = successor
        successor.previous = predecessor
        self.length -= 1

        return self.printList()


    def traverseToIndex(self, index):
        # Check params
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode.next
            counter += 1

        return currentNode

    def printList(self):
        array = []
        currentNode = self.head
        while (currentNode != None):
            array.append(currentNode.value)
            currentNode = currentNode.next

        return array

myLinkedList = DoublyLinkedList()

print("Append: ")

print(myLinkedList.append(10))
print(myLinkedList.append(5))
print(myLinkedList.append(16))

print("\n")
print("Tracking: ")

print(myLinkedList.length)

print(myLinkedList.head.value)
print(myLinkedList.head.next.value)
print(myLinkedList.tail.value)
print(myLinkedList.tail.next)

print("Prepend: ")

print(myLinkedList.prepend(100))
print(myLinkedList.prepend(50))
print(myLinkedList.prepend(2))

print("\n")
print("Tracking: ")

print(myLinkedList.length)

print(myLinkedList.head.value)
print(myLinkedList.head.next.value)
print(myLinkedList.tail.value)
print(myLinkedList.tail.next)

print("List: ")
print(myLinkedList.printList())

print("Insert: ")
print(myLinkedList.insert(200, 99))

print("List: ")
print(myLinkedList.printList())


print("Insert: ")
print(myLinkedList.insert(2, 45))

print("Remove: ")
print(myLinkedList.remove(6))
print(myLinkedList.length)