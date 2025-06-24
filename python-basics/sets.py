# Sets

my_sets={1,2,3,4,5}

print(my_sets)

# adding a new set item
my_sets.add(6)
print(my_sets)

# Removing an item from our set
my_sets.remove(3)
print(my_sets)

# New sets

set1={1,2,3}
set2={3,4,5,6}

# Union method
newSet=set1.union(set2)
print(newSet)

# Interception method
inter_set=set2.intersection(set1)
print(inter_set)

# Difference Method
dif_set=set1.difference(set2)
print(dif_set)