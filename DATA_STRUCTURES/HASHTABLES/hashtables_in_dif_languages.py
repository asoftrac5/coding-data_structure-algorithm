"""
### Notes on Hash Tables: Key and Value Types, Maps, and Sets

#### **Key and Value Flexibility in Hash Tables**:
1. **Key-Value Pair Flexibility**:
   - **Values**: Can be of any data type, including:
     - Functions
     - Objects
     - Arrays
     - Numbers
     - Strings
   - **Keys**: 
     - Traditional hash tables can also use various data types, but JavaScript objects restrict keys to strings.

2. **JavaScript Objects**:
   - In traditional JavaScript objects:
     - Non-string keys (e.g., numbers, functions) are automatically converted to strings.
   - Objects are unordered, meaning key insertion order is not preserved.

---

#### **Maps and Sets in JavaScript (Introduced in ES6)**:
1. **Maps**:
   - **Definition**: A hash table-like structure that allows keys of any data type.
   - **Advantages**:
     - Keys can be any type (e.g., functions, arrays, numbers).
     - Maintains **insertion order** of key-value pairs.
   - **Example**:
     ```javascript
     const myMap = new Map();
     myMap.set('key1', 'value1');
     myMap.set([1, 2], 'value2');
     myMap.set(function() {}, 'value3');
     console.log(myMap);
     ```

2. **Sets**:
   - **Definition**: A hash table-like structure that stores unique keys without associated values.
   - **Example**:
     ```javascript
     const mySet = new Set();
     mySet.add('key1');
     mySet.add('key2');
     console.log(mySet);
     ```

---

#### **Differences Between Maps and Objects**:
1. **Key Types**:
   - **Objects**: Keys are restricted to strings (non-string keys are converted to strings).
   - **Maps**: Keys can be any data type (e.g., functions, arrays).

2. **Order**:
   - **Objects**: Do not maintain insertion order.
   - **Maps**: Preserve insertion order.

---

#### **Practical Example: Map Benefits**:
- Maps are ideal when:
  - You need to use non-string keys.
  - You want to maintain the insertion order of entries.
  - You need better performance for frequent additions and lookups.

---

#### **Building Your Own Hash Table**:
- To deepen understanding, implementing a hash table from scratch is recommended.
- A custom implementation helps clarify how keys, values, collisions, and memory mapping work.
"""