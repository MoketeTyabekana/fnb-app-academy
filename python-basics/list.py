# Lists

# Declaring and printing the list
fruits=["Banana","Apple","Cherry"]
print(fruits[0])

# Inserting a new item at a specific
fruits[1]="Blueberry"
print(fruits[1])

# Removing Items from the list.
fruits.remove(fruits[0])
print(fruits)

# Adding a new item into the list.
fruits.append("Kiwi")
print(fruits)


# Adding new item into a specific position.
fruits.insert(0,"Orange")
print(fruits)

# Sorting out the list items
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)


