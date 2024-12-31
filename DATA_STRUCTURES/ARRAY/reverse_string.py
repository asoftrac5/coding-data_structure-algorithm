# Create a function that reverses a string
# "Hi My name is Asoft." should be:
# "tfosA si eman yM iH"

# Approach 1
def reverse(string):
    # Check for the input
    if not string or len(string) < 2 or not isinstance(string, str):
        return "It isn't a string"
    
    cha_str = list(string)
    reverse_list = []
    for c in cha_str[::-1]:
        reverse_list.append(c)
    
    reverse_string = ('').join(reverse_list)
    return reverse_string

string_eg = 'Software Engineer!'
print(reverse(string_eg))

string_eg = '!'
print(reverse(string_eg))

#Approach 2
def reverse1(string):
    cha_str = list(string)
    reverse_list = reversed(cha_str)
    reverse_string = ('').join(reverse_list)
    return reverse_string

string_eg1 = 'Software Engineer!'
print(reverse1(string_eg1))


# Approach 3
def reverse2(string):
    return string[::-1]

print(reverse2(string_eg1))