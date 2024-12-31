obj1 = {"software": True}

obj2 = obj1

obj1["software"] = "engineer"

del obj1

obj2 = "Success"

# print("1: ", obj1)
print("2: ", obj2)

"""
### **Important Notes on Pointers**

#### **Definition of a Pointer**
- A pointer is a reference to another location in memory, object, or node.
- It does not create a copy; instead, it points to the same memory location.

#### **Demonstration in JavaScript**
1. **Object Example:**
   - Creating a pointer:
     ```javascript
     const object1 = { a: true };
     const object2 = object1;
     ```
     Both `object1` and `object2` reference the same memory location.
   - If `object1.a` is updated, the change is reflected in `object2` because they point to the same object.
2. **Changing Values:**
   - Updating a pointer affects all variables referencing the same memory.

#### **Garbage Collection in JavaScript**
- **Automatic Memory Management:**
  - JavaScript removes unused memory (garbage collection).
  - If no pointers reference a memory location, it is automatically freed.
  - Example:
    ```javascript
    let object1 = { a: "value" };
    let object2 = object1;
    object2 = "new value"; // The original object is garbage collected.
    ```
- Memory is not deleted if there are still references pointing to it.

#### **Manual Memory Management in Low-Level Languages**
- **Non-Garbage Collected Languages (e.g., C, C++):**
  - Programmers must manually manage memory.
  - If unused memory is not explicitly freed, it can lead to **memory leaks**.
- **Benefits of Manual Management:**
  - Greater control allows for optimized performance and efficient memory usage.

#### **Advantages of Garbage Collection**
- Automatic deletion of unreferenced objects.
- Reduces the risk of memory leaks for the programmer.

#### **Key Applications in Linked Lists**
- In linked lists:
  - Nodes are connected using pointers.
  - When a node is deleted, its pointer is updated to remove references to it, making it eligible for garbage collection.

#### **Summary**
- A pointer is simply a reference to a memory location.
- In garbage-collected languages like JavaScript:
  - Memory management is automatic.
  - Unreferenced objects are deleted.
- In low-level languages:
  - Manual memory management is required, offering more control but with increased risk of errors.
- Pointers play a critical role in data structures like linked lists, enabling dynamic memory allocation and efficient data management.
"""