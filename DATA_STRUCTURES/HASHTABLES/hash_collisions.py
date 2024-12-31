def wow():
    print("Wowwwwww!!!")

user = {
    "age": 54,
    "name": "kylie",
    "magic": True,
    "scream": wow
}

print(user["age"]) # O(1) # Lookup/access
user["spell"] = "abra kadabra" # O(1) : Insert
print(user)

print(user['scream'])


"""
### Important Notes on Hash Tables: Performance and Collisions

#### **Key Operations and Their Time Complexities**:
1. **Insertion**:
   - Time complexity: $$O(1)$$.
   - The key is hashed, and the data is placed directly into the calculated memory address.
   
2. **Lookup**:
   - Time complexity: $$O(1)$$.
   - The key is hashed to retrieve the value from the memory address.

3. **Deletion**:
   - Time complexity: $$O(1)$$.
   - The key is hashed to locate the memory address, and the value is removed without shifting indexes, unlike arrays.

4. **Search**:
   - Time complexity: $$O(1)$$.
   - The hash function locates the key’s memory address directly.

---

#### **Demonstration**:
- Objects in JavaScript can store properties like `age`, `name`, and methods.
- Example:
  ```javascript
  let user = {
      age: 54,
      name: "Kylie",
      magic: true,
      scream: function() {
          console.log("Ahhh!");
      }
  };
  ```
- Properties and methods are accessed or modified with $$O(1)$$ complexity using hash functions.

---

#### **Hash Tables and Memory**:
1. **Memory Allocation**:
   - Hash tables are allocated a fixed memory space (e.g., 12 slots).
   - Data is distributed across memory addresses using a hash function.

2. **Collisions**:
   - Occur when multiple keys are hashed to the same memory address.
   - Example: Hashing "John Smith" and "Sandra Dee" results in the same address.

---

#### **Collision Handling**:
1. **Separate Chaining**:
   - Uses a secondary data structure, like a linked list, to store multiple entries at the same address.
   - Example: Both "John Smith" and "Sandra Dee" are stored in a bucket at the same address.

2. **Other Methods**:
   - **Open Addressing**: Finds the next available slot in memory for the new data.
   - **Robin Hood Hashing**: Balances the placement of keys to minimize long chains.
   - **Many more** (refer to collision resolution strategies for details).

---

#### **Impact of Collisions**:
1. **Performance**:
   - Collisions can degrade hash table operations from $$O(1)$$ to $$O(n/k)$$, where $$k$$ is the hash table size.
   - With simplification, this becomes $$O(n)$$ in the worst-case scenario.
   
2. **Mitigation**:
   - Optimized hash functions aim to minimize collisions by evenly distributing data across memory.
   - However, collisions are unavoidable with large datasets and limited memory.

---

#### **Key Takeaways**:
- Hash tables are incredibly fast for insertion, lookup, deletion, and search.
- Collisions are a natural downside, but modern hash table implementations use efficient strategies to mitigate their impact.
- Understanding collision resolution methods like separate chaining and open addressing is crucial for discussing hash tables in interviews.
- Hash tables balance speed and memory efficiency, making them indispensable in data structure design.
"""