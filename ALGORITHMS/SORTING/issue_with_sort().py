letters = ['a', 'd', 'z', 'e', 'r', 'b']
basket = [2, 65, 34, 2, 1, 7, 8]

sorted_letters = sorted(letters)
print(sorted_letters)
sorted_basket = sorted(basket)
print(sorted_basket)

"""
### Important Notes on Sorting Specific to JavaScript (and General Principles)

1. **Sorting Algorithms Across Languages**:
   - Sorting can be applied to any data type, not just numbers or strings.
   - It’s crucial to understand how built-in sorting methods work in the language you're using.

2. **JavaScript’s `sort()` Method**:
   - By default, the `sort()` method converts elements to strings and compares their Unicode values.
   - This behavior can lead to unexpected results when sorting numbers:
     - Example: `[65, 34, 2]` might be sorted as `[2, 34, 65]` based on Unicode values.

3. **Character Code Comparison**:
   - The `charCodeAt` method can reveal how characters are being compared.
   - Unicode values determine the order in default string-based sorting.

4. **Sorting Complexities**:
   - The time and space complexity of `sort()` is implementation-dependent in JavaScript.
   - Different browsers (Chrome, Firefox, Safari) use varying engines and sorting algorithms.

5. **Language-Specific Sorting**:
   - Sorting behavior can differ based on character sets and languages:
     - Example: Spanish words with accented characters might sort incorrectly without adjustments.
   - To address this, use functions like `localeCompare` for proper internationalized sorting.

6. **Custom Sorting with Callback Functions**:
   - Define a comparator function to handle custom sorting:
     - For numbers: `(a, b) => a - b`
     - For strings in specific locales: `(a, b) => a.localeCompare(b)`

7. **Considerations for Built-in Methods**:
   - Always read documentation for built-in methods to understand how they work.
   - Be aware of implementation differences and their potential impact on results.

8. **Why Learn Sorting in Depth**:
   - Built-in methods rely on standard algorithms, but understanding their mechanics allows you to:
     - Debug unexpected results.
     - Optimize sorting for large datasets or specific use cases.
     - Ace coding interviews by explaining how sorting algorithms work.

9. **Sorting Demonstrations**:
   - Example 1: Sorting Numbers:
     ```javascript
     const numbers = [65, 34, 2];
     const sortedNumbers = numbers.sort((a, b) => a - b); // Proper numerical sort
     console.log(sortedNumbers); // Output: [2, 34, 65]
     ```
   - Example 2: Sorting Spanish Words:
     ```javascript
     const words = ["árbol", "costa", "fútbol"];
     const sortedWords = words.sort((a, b) => a.localeCompare(b)); // Locale-aware sorting
     console.log(sortedWords); // Output: ["árbol", "costa", "fútbol"]
     ```

10. **Upcoming Topics**:
    - Learn common sorting algorithms used in computer science.
    - Understand their trade-offs and use cases.
    - Discuss how these algorithms work under the hood of methods like `sort()`.
"""