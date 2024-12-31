class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None
    
    def keys(self):
        key_list = []
        for i in range(len(self.data)):
            if self.data[i]:
                key_list.append(self.data[i][0][0])

        return key_list
    
    def _hash(self, key):
        hash = 0
        for i, char in enumerate(key):
            hash = (hash + ord(char) * i) % len(self.data)
        return hash
    

MyHash = HashTable(50)
print(MyHash.set('software', 100))
print(MyHash.set('engineer', 200))
print(MyHash.set('engineer', 400))

print(MyHash.get('engineer'))

print(MyHash.keys())


"""
### Notes: Hash Table Implementation Walkthrough

#### Key Concepts:
1. **Private Properties with `_` Prefix**:
   - In languages like Java, private properties are truly inaccessible outside the class. 
   - In JavaScript, the `_` prefix is a developer standard to indicate private properties or methods (e.g., `_hash`).
   - This is not enforced by JavaScript; developers can still access these properties.

2. **Hash Function Explanation**:
   - Converts a string key into an index for the hash table.
   - Works by:
     - Initializing `hash = 0`.
     - Iterating through each character of the key, calculating its UTF-16 character code (`charCodeAt` in JS or `ord` in Python).
     - Multiplying the character code by its index for uniqueness.
     - Using the modulo operator (`%`) to constrain the value within the table's size.
   - Example: For the key `grapes`, the hash value is calculated to fit within the table size (e.g., 50 slots).

3. **Key Operations**:
   - **Set (`set`)**:
     - Takes a key and value.
     - Computes the hash to determine the address.
     - Handles collisions by storing key-value pairs in a bucket (an array) at the hashed address.
     - If no bucket exists, initializes a new array at the address.
     - Adds the key-value pair to the bucket using `.append()` or `.push()`.
   - **Get (`get`)**:
     - Takes a key to retrieve its value.
     - Computes the hash to find the address.
     - Checks if the bucket at that address exists.
     - Iterates through the bucket to find the matching key and returns its value.
     - Returns `None` if the key is not found.

4. **Collision Handling**:
   - When multiple keys hash to the same address, they are stored in a bucket (array) at that address.
   - To retrieve a value, iterate through the bucket to find the correct key.

5. **Time Complexity**:
   - **Hash Function**: O(1) for good hash functions.
   - **Set/Get Operations**:
     - Best Case: O(1) (no collisions).
     - Worst Case: O(n) (all keys collide, resulting in a single bucket).
     - Real-life scenarios: Typically O(1) if collisions are minimized.

6. **Demonstration Example**:
   ```python
   class HashTable:
       def __init__(self, size):
           self.data = [None] * size

       def set(self, key, value):
           address = self._hash(key)
           if not self.data[address]:
               self.data[address] = []
           self.data[address].append([key, value])
           return self.data

       def get(self, key):
           address = self._hash(key)
           current_bucket = self.data[address]
           print("current bucket: ", current_bucket)
           if current_bucket:
               for i in range(len(current_bucket)):
                   if current_bucket[i][0] == key:
                       return current_bucket[i][1]
           return None

       def _hash(self, key):
           hash = 0
           for i, char in enumerate(key):
               hash = (hash + ord(char) * i) % len(self.data)
           return hash

   # Usage
   myHashTable = HashTable(50)
   print(myHashTable.set('grapes', 10000))  # Adds 'grapes' with value 10000
   print(myHashTable.set('apples', 20000))  # Adds 'apples' with value 20000
   print(myHashTable.set('apples', 40000))  # Updates 'apples' value to 40000
   print(myHashTable.get('grapes'))         # Retrieves value of 'grapes' (10000)
   ```

7. **Key Observations**:
   - **Collisions**: Example shows collisions when table size is small.
   - **Bucket Management**: Each bucket is an array that may contain multiple key-value pairs.
   - **Data Loss**: Without proper collision handling, new values may overwrite existing ones.

8. **Next Steps**:
   - Learn about other operations like traversing all keys in the hash table.
   - Improve hash functions and explore alternative collision-resolution strategies (e.g., chaining, open addressing).
"""



































# class HashTable:
#     def __init__(self, size):
#         self.data = [None] * size

#     # Function to set the key-value pair in the hash table
#     def set(self, key, value):
#         address = self._hash(key)
#         if not self.data[address]:
#             self.data[address] = []
        
#         self.data[address].append([key, value])

#         return self.data

#     # Function to get the value from the hash table
#     def get(self, key):
#         address = self._hash(key)
#         current_bucket = self.data[address]
#         print("current bucket: ", current_bucket)
#         if current_bucket:
#             for i in range(len(current_bucket)):
#                 if current_bucket[i][0] == key:
#                     return current_bucket[i][1]
        
#         return None

        
#     def _hash(self, key):
#         hash = 0  # Avoid naming conflicts with the built-in `hash` function
#         for i, char in enumerate(key):
#             hash = (hash + ord(char) * i) % len(self.data)
#         return hash

    
# myHashTable = HashTable(50)
# print(myHashTable.set('grapes', 10000))
# print(myHashTable.set('apples', 20000))
# print(myHashTable.set('apples', 40000))
# print(myHashTable.get('grapes'))
