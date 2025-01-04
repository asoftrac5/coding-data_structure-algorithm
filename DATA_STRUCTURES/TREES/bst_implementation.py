class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        
        else:
            current = self.root
            while True:
                if value < current.value:
                    if not current.left:
                        current.left = node
                        return self
                    current = current.left
                
                if value > current.value:
                    if not current.right:
                        current.right = node
                        return self
                    current = current.right

    def lookup(self, value):
        if not self.root:
            return None
        
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif value == current.value:
                return current
    
        return None
    
    def remove(self, value):
        node = Node(value)
        if not self.root:
            return False
        
        current = self.root
        parent = None
        while current:
            if value < current.value:
                parent = current
                if not current.left:
                    return False
                
                current = current.left

            elif value > current.value:
                parent = current
                if not current.right:
                    return False
                
                current = current.right

            elif value == current.value:
                # We have a match, get to work 
                
                # Option 1: No righ child:
                if current.right == None:
                    # if current == parent.right:
                    #     parent.right = current.left
                    # elif current == parent.left:
                    #     parent.left = current.left
                    if parent == None:
                        self.root = current.left
                    
                    else:
                        # If parent > current value, make current left child a left child of parent
                        if current.value < parent.value:
                            parent.left = current.left

                        # If parent < current value, make current left child a right child of parent
                        elif current.value > parent.value:
                            parent.right = current.left

                # Option 2: Right child which doesn't have a left child

                elif current.right.left == None:
                    if parent == None:
                        self.root = current.left

                    else:
                        # If parent > current value, make current left child a left child of parent
                        if current.value < parent.value:
                            parent.left = current.right

                        # If parent < current value, make current left child a right child of parent
                        elif current.value > parent.value:
                            parent.right = current.right

                # Option 3: Right child that has a left child
                else:
                    # Find the right child's left most child
                    leftmost = current.right.left
                    leftmostParent = current.right
                    while(leftmost.left != None):
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = current.left
                    leftmost.right = current.right

                    if (parent == None):
                        self.root = leftmost

                    else:
                        if current.value < parent.value:
                            parent.left = leftmost
                        elif current.value > parent.value:
                            parent.right = leftmost

                return True



def traverse(node):
    tree = {"value": node.value}
    tree["left"] = None if node.left is None else traverse(node.left)
    tree["right"] = None if node.right is None else traverse(node.right)
    return tree

tree = BinarySearchTree()
print("Insert: ")
print(tree.insert(9))
print(tree.insert(4))
print(tree.insert(6))
print(tree.insert(20))
print(tree.insert(170))
print(tree.insert(15))
print(tree.insert(1))
print(traverse(tree.root))
print("Look up: ")
print(tree.lookup(80))
# print(tree.lookup(170).left.value)
# print(tree.lookup(170).right.value)

print(tree.remove(9))

print(traverse(tree.root))


"""
class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        
        else:
            current = self.root

            while True:
                if value < current.value:
                    if not current.left:
                        current.left = node
                        return self
                    current = current.left
                else:
                    if not current.right:
                        current.right = node
                        return self
                    current = current.right


    def lookup(self, value):

        if not self.root:
            return None
        
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif value == current.value:
                return current
            
        return None
"""