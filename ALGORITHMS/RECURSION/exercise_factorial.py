# Write two functions that finds the factorial of any number. 
# One should use recursive, the other should just use a for loop

def findFactorialRecursive(number): # O(n)
    # code here
    # Base case
    if number == 2:
        return 2
    
    # Recursive case
    return number * findFactorialRecursive(number - 1)

print(findFactorialRecursive(5))

def findFactorialIterative(number): # O(n)
    # code here
    # answer = number
    # while number > 1:
    #     answer = answer * (number - 1)
    #     number = number - 1
    # return answer

    answer = 1
    # Base case
    if number == 2:
        answer = 2
    for i in range(2, number + 1):
        answer = answer * i

    return answer

print(findFactorialIterative(5))