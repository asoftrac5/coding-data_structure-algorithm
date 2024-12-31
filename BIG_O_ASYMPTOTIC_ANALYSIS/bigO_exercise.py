# What is the Big O of the below function? (Hint: You may want to go line by line)

def funChallenge(input):
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for i in range(len(input)): # O(n)
        
        # anotherFunction() # O(n) # Assuming that the bigO of the function is O(1) as we don't don't the nature of the function
        stranger = True # (n)
        a += 1 # O(n)
    
    return a # O(1)

funChallenge(input)

# Input doesn't matter, it can be an array, a linked list, etc.

# Contant operations outside the loop: O(1) + O(1) + O(1) = O(3)
# Operations inside the loop: O(n) + O(n) + O(n) + O(n) = O(4n)
# Net operations: O(3) + O(4n) = O(3 + 4n)
# The overall complexity is O(n), as the dominant term is the linear iteration through the input