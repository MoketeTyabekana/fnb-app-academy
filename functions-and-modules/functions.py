# functions and modules

def greet(name):
    print(f"Hello, {name}!")
    
    # calling the function
greet("Mokete")


print("\n")
print("---------------------")
# Using the return statement

def add_numbers(a, b):
    return a + b

# calling the function and storing the result
result = add_numbers(5, 3)
print("\n")
print(f"The sum is: {result}")

print("\n")
print("---------------------")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(f"The factorial of 5 is: {factorial(5)}")

print("\n")
print("---------------------")

def greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"
# calling the function with default greeting
print(greeting("Mokete"))

# calling the function with custom greeting    
print(greeting("Mokete", "Welcome"))