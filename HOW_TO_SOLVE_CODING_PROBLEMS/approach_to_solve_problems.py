"""
# What are companies looking for: 
# 1. Analytic skills 
# 2. Coding skills 
# 3. Technical skills 
# 4. Communication skills 

# Data structures: 
# 1. Arrays 
# 2. Stacks 
# 3. Queues 
# 4. Linked Lists 
# 5. Trees 
# 6. Tries 
# 7. Graphs 
# 8. Hash Tables 

# Algorithms: 
# 1. Sorting 
# 2. Dynamic Programming 
# 3. BFS + DFS (Searching) 
# 4. Recursion 

# The 3 pillars of good code: 
# 1. Readable 
# 2. Time Complexity 
# 3. Space Complexity 

# What skills interviewer is looking for: 
# 1. Analytic skills – How do you think through problems and analyze things? 
# 2. Coding skills – Do you code well, by writing clean, simple, organized, readable code? 
# 3. Technical skills – Do you know the fundamentals of the job you’re applying for? 
# 4. Communication skills – Does your personality match the companies’ culture? 
"""
# Step by step through a problem: 

"""
# 1. When the interviewer says the question, write down the key points at the top. (Sorted array, etc...). 
# Make sure you have all the details. Show how organized you are. 

# 2. Make sure you double check: What are the inputs? What are the outputs? What are the outputs? 

# 3. What is the most important value of the problem. Do you have time, and space and memory, etc.. 
# What is the main goal? 

# 4. Don’t be annoying and ask too many questions. 

# 5. Start with the naive/brute force approach. First thing that comes into mind. 
# It shows that you’re able to think well and critically. 
# (You don’t  even need to write this code, just speak about it) 

# 6. Tell them why this approach is not the best (i.e. O(n^2) or higher, not readable, etc...) 

# 7. Walk through your approach, comment things and see where you may be able to break things. 
# Any repetition, bottlenecks like O(n^), or unnecessary works. 
# Did you use all the information that the interview gave you? 
# Bottle next is the part of the code with the   

# 8. Before you start coding, walk through your code and write down the steps you are going to do. 

# 9. Modularize your code from the very beginning. 
# Break up your code into beautiful small pieces and add just comments if you need to. 

# 10. Start actually writing your code now. 
# Keep in mind that the more you prepare and understand what you need to code, the better the whiteboard will go. 
# So never start a whiteboard interview not being  sure of how things are going to work out. 
# That is a disaster. Keep in mind. 

# 11. Think about error checks and how you can break this code. 
# Never make assumptions about the input. Assume people are trying to break your code and that Darth Vader is using your function. 
# How will you safeguard it. 
# Always check for false inputs that you don’t want. Here is a trick: Comment in the code, the checks  

# 12. Don’t use bad/confusing names like i and j. Write code that reads well, 

# 13. Test your code: Check for no parms, 0, undefined, null, massive arrays, asynchronous code, etc... 
# Ask the interviewer if we can make assumptions about 

# 14. Finally talk to the interviewer where you would improve the code. Does it work? 
# Are there approaches? Is it readable? What would you google to improve? 
# How can performance be improved? Poke holes in your code 

# 15. If your interviewer is happy with the solution, the interview usually ends here. 
# It is also common that the interviewer asks you extension questions, 
# such as how you would handle the problem if the whole input were too large to fit into memory.
"""

# Good Code CheckList:

"""
1. It works
2. Good use of data structures
3. Code re-use/ Do not repeat yourself
4. Modular - makes code more readable, maintainable and testable
5. Less than O(N^2). We want to avoid nestecd loops if we can since they are O(n^2). 
Two separate loops are better than 2 nested loops.
6. Low space complexity --> Recursion can cause stack overflow, copying of large arrays 
may exceed memory of machine.
"""

# Heuristics to ace the question:

"""
1. Hash Tables are usually the answer to improve Time Complexity
2. If it's a sorted array, use Binary tree to achieve O(log N). Divide and Conquer -
Divide a data set into smaller chunks and then repeating a process
3. Try sorting your input.
4. Hash tables and precomputed information (i.e., sorted) are some of the best ways to
optimize your code.
5. Look at the Time vs Space tradeoff. Sometimes storing extra state in memory can help
the time. (Runtime)
6. If the interviewer is giving you advice/tips/hints follow them.
7. Space time tradeoffs: Hastables usually solve this a lot of times. You use more space,
but you can get a time optimization to the process. 
"""

# And always remember: Communicate your thought process as much as possible. 
# Don't worry about finishing it fast.