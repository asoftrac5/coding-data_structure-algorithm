# 10 --> 5 --> 16

# Structure
# myLinkedList = {
#     "value": 10,
#     "next": {
#         "value": 5,
#         "next": {
#             "value": 16,
#             "next": None
#         }
#     }
# }

# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def append(self, value):
#         node = Node(value)
#         if not self.head:
#             self.head = node
#             self.tail = self.head
#             self.length += 1
        
#         else:
#             self.tail.next = node
#             self.tail = node
#             self.length += 1

#         return node.value, node.next
    
#     def prepend(self, value):
#         node = Node(value)
#         if not self.head:
#             self.head = node
#             self.tail = node
#             self.length += 1
#         else:
#             node.next = self.head
#             self.head = node
#             self.length += 1

#         return node.value, node.next
    
#     def insert(self, index, value):
#         # check params
#         if index >= self.length:
#             return self.append(value)
        
#         if index < 0:
#             return self.prepend(value)

#         node = Node(value)
#         # *   *
#         #  \ /
#         #   *
#         leader = self.traverseToIndex(index - 1)
#         holdingPointer = leader.next
#         leader.next = node
#         node.next = holdingPointer
#         self.length += 1
#         return self.printList()
    
#     def remove(self, index):
#         # leader = self.traverseToIndex(index - 1)
#         # successor = self.traverseToIndex(index + 1)
#         # leader.next = successor

#         # Or

#         leader = self.traverseToIndex(index - 1)
#         node_to_remove = leader.next
#         successor = node_to_remove.next
#         leader.next = successor
#         self.length -= 1

#         return self.printList()


#     def traverseToIndex(self, index):
#         # Check params
#         counter = 0
#         currentNode = self.head
#         while counter != index:
#             currentNode = currentNode.next
#             counter += 1

#         return currentNode

#     def printList(self):
#         array = []
#         currentNode = self.head
#         while (currentNode != None):
#             array.append(currentNode.value)
#             currentNode = currentNode.next

#         return array

# print("Append: ")

# print(myLinkedList.append(10))
# print(myLinkedList.append(5))
# print(myLinkedList.append(16))

# print("\n")
# print("Tracking: ")

# print(myLinkedList.length)

# print(myLinkedList.head.value)
# print(myLinkedList.head.next.value)
# print(myLinkedList.tail.value)
# print(myLinkedList.tail.next)

# print("Prepend: ")

# print(myLinkedList.prepend(100))
# print(myLinkedList.prepend(50))
# print(myLinkedList.prepend(2))

# print("\n")
# print("Tracking: ")

# print(myLinkedList.length)

# print(myLinkedList.head.value)
# print(myLinkedList.head.next.value)
# print(myLinkedList.tail.value)
# print(myLinkedList.tail.next)

# print("List: ")
# print(myLinkedList.printList())

# print("Insert: ")
# print(myLinkedList.insert(200, 99))

# print("List: ")
# print(myLinkedList.printList())


# print("Insert: ")
# print(myLinkedList.insert(2, 45))

# print("Remove: ")
# print(myLinkedList.remove(6))
# print(myLinkedList.length)


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = self.head
            self.length += 1

            return self.printList()

        if self.length > 0:
            self.tail.next = node
            self.tail = node
            node.next = None
            self.length += 1

            return self.printList()
        
    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1

            return self.printList()
        
        if self.length > 0:
            node.next = self.head
            self.head = node
            self.length += 1

            return self.printList()
        
    def insert(self, index, value):
        # check params
        if index >= self.length:
            return self.append(value)

        if index < 0:
            return self.prepend(value)
        
        # *   *
        #  \ /
        #   *

        node = Node(value)

        leader = self.traverseToIndex(index - 1)
        holdingPointer = leader.next
        leader.next = node
        node.next = holdingPointer
        self.length += 1

        return self.printList()
    
    def remove(self, index):
        # Check params
        if index < 0 and index > self.length:
            return None
        
        leader = self.traverseToIndex(index - 1)
        node_to_be_removed = leader.next
        leader.next = node_to_be_removed.next
        self.length -= 1
        return self.printList()
    
    def traverseToIndex(self, index):
        currentNode = self.head
        counter = 0

        while counter != index:
            currentNode = currentNode.next
            counter += 1

        return currentNode

    def printList(self):
        linked_list = []
        currentNode = self.head
        
        while currentNode != None:
            linked_list.append(currentNode.value)
            currentNode = currentNode.next
        
        return linked_list

myLinkedList = LinkedList()

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

print("Insert: ")
print(myLinkedList.insert(2, 45))

print("Remove: ")
print(myLinkedList.remove(6))
print(myLinkedList.length)