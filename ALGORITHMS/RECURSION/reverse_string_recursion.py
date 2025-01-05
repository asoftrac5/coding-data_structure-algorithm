# Normal Approach
def reverseString(str):
    # Simple approach
    # return str[::-1]

    # Better approach
    reverse_arr = []
    for i in str[::-1]:
        reverse_arr.append(i)
    reverse_str = "".join(reverse_arr)
    return reverse_str

print(reverseString("yoyo master"))

# Recursive Approach
def reverseStringRecursive(str):
    # Base case
    if str == "":
        return ""
    
    return reverseStringRecursive(str[1:]) + str[0]

print(reverseStringRecursive("yoyo master"))