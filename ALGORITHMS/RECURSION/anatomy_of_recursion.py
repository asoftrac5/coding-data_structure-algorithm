"""
### Important Notes on Recursion: Base Case and Return Values  

1. **Every Recursive Function Needs a Base Case**:  
   - The **base case** is a condition that stops the recursion.  
   - Without a base case, the function will continue infinitely, causing a **Stack Overflow**.

2. **Recursive Function Structure**:  
   - **Base Case**: Defines when to stop the recursion.  
   - **Recursive Case**: The logic to call the function again.  
   - Example:  
     ```javascript
     function inception(counter = 0) {
         if (counter > 3) return "done"; // Base Case
         return inception(counter + 1); // Recursive Case
     }
     ```

3. **The Role of the Call Stack**:  
   - Each recursive call adds a new frame to the call stack.  
   - Once the base case is met, the stack starts **"popping"** off frames, returning the values step-by-step.  

4. **Understanding Return Values in Recursion**:  
   - If a recursive function doesn't explicitly return a value, it defaults to `undefined`.  
   - To ensure the result "bubbles up" through the recursion, you must `return` the recursive call's result.  
   - Example:
     ```javascript
     return inception(counter + 1); // Ensures values propagate upward
     ```

5. **Debugging Recursive Functions**:  
   - Use the `debugger` keyword to inspect variable states and the call stack at each step.  
   - Observe how the call stack grows with each recursive call and how it shrinks after the base case is reached.

6. **Key Insights for Writing Recursive Functions**:  
   - **Base Case**: Clearly define when recursion should stop.  
   - **Recursive Case**: Ensure the function progresses toward the base case.  
   - **Returns**: Always return values from both the base and recursive cases to propagate results correctly.

7. **Common Pitfalls in Recursion**:  
   - Missing a base case leads to infinite recursion and Stack Overflow.  
   - Forgetting to return values results in `undefined` bubbling up through the stack.  
   - Recursive functions must move closer to the base case with each call.

8. **Key Steps for Writing Recursive Functions**:  
   1. **Identify the base case**: Define when recursion stops.  
   2. **Identify the recursive case**: Determine when and how to call the function again.  
   3. **Progress toward the base case**: Ensure each recursive call gets closer to stopping.  
   4. **Return values properly**: Use `return` to propagate results through the stack.

9. **Illustration Example**:  
   - A counter incremented with each recursive call.  
   - Stops recursion when the counter exceeds 3:  
     ```javascript
     function inception(counter = 0) {
         if (counter > 3) return "done"; // Base case
         return inception(counter + 1); // Recursive case
     }
     inception(); // Returns "done"
     ```

10. **Debugging Insights**:  
    - Step-by-step debugging shows the flow:  
      - Call stack grows with each recursive call.  
      - Base case triggers `return`, starting to "pop" calls off the stack.  
      - Values propagate upward through the stack until the original call receives the result.

11. **Practical Application**:  
    - Practice recursive problems to solidify understanding.  
    - Ensure every recursive function adheres to the three key rules:  
      1. Base case.  
      2. Recursive case.  
      3. Proper returns for value propagation.  

With these principles, you can confidently build and debug recursive functions!
"""

def inception(count):
    if count > 3:
        return "done!"
    count += 1
    return inception(count)

print(inception(0))
