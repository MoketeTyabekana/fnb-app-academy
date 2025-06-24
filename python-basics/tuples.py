# Tuplets: They allow duplication, order function and cannot be changed.

tuplets=(1,2,3,4,5)
print(tuplets)

# Print a single item
print(tuplets[2])

# Using negation index to get a specific item
print(tuplets[-1])

# Combing two tuplets together.

t1=(1,2,3)
t2=(4,5,6)

newtuplets=t1+t2
print(newtuplets)