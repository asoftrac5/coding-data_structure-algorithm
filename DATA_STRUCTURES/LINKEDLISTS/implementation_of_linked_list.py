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
        if not self.head:
            self.head = node
            self.tail = self.head
            self.length += 1
        
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

        return node.value, node.next

myLinkedList = LinkedList()

print(myLinkedList.append(10))
print(myLinkedList.append(5))
print(myLinkedList.append(16))

print(myLinkedList.length)
print(myLinkedList.length)