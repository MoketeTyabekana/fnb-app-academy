# Strings

message = """Hello, World!
is cool"""
# 
print(message)

# advanced string formatting
name = " Alice"
# Accessing the first character
print(name[0])  
print(name[3])

# string length
print(len(name))

# using strip to remove leading and trailing spaces

print(name.strip())

# using lower to convert to lowercase
print(name.lower())

# using upper to convert to uppercase
print(name.upper())

# using replace to replace a substring
print(name.replace("Alice", "Bob"))

# using split to split a string into a list
print(message.split())