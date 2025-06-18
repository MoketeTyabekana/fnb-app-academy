# loops
# for loop, while loop, range function
# for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# while loop is used to execute a block of code as long as a condition is true.


cars= ["Toyota", "Honda", "Ford", "Chevrolet"]

for car in cars:
    if car == "Ford":
        break
    print(car)
    
for car in cars:
 if car == "Ford":
  continue
print(car)