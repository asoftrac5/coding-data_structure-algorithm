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

    def breadthFirstSearch(self):
        currentNode = self.root
        list = []
        queue = []

        queue.append(currentNode)
        while len(queue) > 0:
            currentNode = queue.pop(0)
            print(currentNode.value)

            list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        return list


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

# print(tree.remove(9))

print(traverse(tree.root))

print("BFS: ")

print(tree.breadthFirstSearch())


"""
### Important Notes on Breadth-First Search (BFS)

1. **Concept**:
   - BFS traverses a tree or graph level by level, starting from the root.
   - It visits all the nodes at the current level before moving to the next level.

2. **Data Structure Used**:
   - A **queue** is essential for BFS to keep track of nodes to visit at the current level and revisit their children.

3. **Memory Usage**:
   - BFS requires memory to store all the child nodes of the current level in the queue. This can lead to high memory consumption, especially with wide trees.

4. **Traversal Path**:
   - The order of traversal for BFS in a tree is typically:
     - Root → Left Child → Right Child → Children of Left → Children of Right → and so on.

5. **Steps in BFS**:
   - Start with the root node and add it to the queue.
   - For each node, remove it from the queue, process it, and add its children (left and right) to the queue.
   - Repeat until the queue is empty.

6. **Advantages**:
   - BFS is ideal for finding the shortest path in an unweighted graph or tree.
   - It processes nodes level by level, which can be useful for certain problems like finding all nodes at a particular depth.

7. **Disadvantages**:
   - High memory consumption due to the need to store all child nodes of a level in the queue.
   - Inefficient for trees with many levels but sparse nodes.

8. **Applications**:
   - Finding the shortest path in unweighted graphs.
   - Level-order traversal of binary trees.
   - Solving problems where visiting nodes level by level is required. 

9. **Key Points to Remember**:
   - BFS uses a **queue** to manage the traversal order.
   - Memory consumption grows with the width of the tree or graph, as the queue size depends on the number of child nodes at a level.
   - BFS is simple to implement and ensures that all nodes at one depth are visited before moving to the next.
"""