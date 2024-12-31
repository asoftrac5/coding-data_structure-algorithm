# What is the Big O of the below function? (Hing: You may want to go line by line)

def anotherFunChallenge(input):
    a = 5 # O(1)
    b = 10 # O(1)
    c = 50 # O(1)

    for i in range(len(input)): # O(n) # We can either include or exclude it
        x = i + 1 # O(n)
        y = i + 2 # O(n)
        z = i + 3 # O(n)

    for j in range(len(input)): # O(n) # We can either include or exclude it
        p = j * 2 # O(n)
        q = j * 2 # O(n)

    whoAmI = "I don't know" # O(1)

# O(4) + O(7n) = O(4 + 7n) = O(n)